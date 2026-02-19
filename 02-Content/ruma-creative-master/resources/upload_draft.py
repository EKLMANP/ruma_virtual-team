#!/usr/bin/env python3
"""
RUMA Creative Master - 自動上傳文章草稿 v2 至 RUMA 官網
用途：將 Content Alchemist 產出的文章 Markdown 上傳至 Supabase news 資料表（草稿狀態）
      Eric 審核通過後，透過 Telegram 回覆「發布」觸發正式發布

使用方式：
  python upload_draft.py --article articles/dragon-boat-beginner-guide
  python upload_draft.py --publish {news_id}
"""

import os
import re
import json
import hmac
import hashlib
import argparse
import requests
from datetime import datetime, timezone
from pathlib import Path
from typing import Optional
from dotenv import load_dotenv

# ── 載入環境變數 ──────────────────────────────────────────────────────────────
load_dotenv(Path(__file__).parent.parent.parent / ".env")  # 02-Content/.env

SUPABASE_URL = os.getenv("SUPABASE_URL", "https://tmhlxhkzmssqnptmqzhy.supabase.co")
SUPABASE_SERVICE_ROLE_KEY = os.getenv("SUPABASE_SERVICE_ROLE_KEY")
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")
PREVIEW_SECRET = os.getenv("PREVIEW_SECRET", "")
RUMA_SITE = "https://uat.rumadragonboat.com"  # UAT 環境

SUPABASE_HEADERS = {
    "Content-Type": "application/json",
    "apikey": SUPABASE_SERVICE_ROLE_KEY,
    "Authorization": f"Bearer {SUPABASE_SERVICE_ROLE_KEY}",
    "Prefer": "return=representation"
}




# ── Markdown 解析 ─────────────────────────────────────────────────────────────

def parse_frontmatter(content: str):
    """解析 Markdown frontmatter（YAML 區塊）"""
    meta = {}
    body = content
    if content.startswith("---"):
        parts = content.split("---", 2)
        if len(parts) >= 3:
            for line in parts[1].strip().splitlines():
                if ":" in line:
                    key, _, val = line.partition(":")
                    meta[key.strip()] = val.strip().strip('"\'')
            body = parts[2].strip()
    return meta, body


def markdown_to_content_blocks(md_text: str) -> list[dict]:
    """
    將 Markdown 文字轉換為 Supabase content JSON 陣列格式
    支援：段落、H1-H4、圖片、無序列表、有序列表、引用、水平線
    """
    blocks = []
    lines = md_text.splitlines()
    i = 0
    list_buffer = []
    list_type = None

    def flush_list():
        nonlocal list_buffer, list_type
        if list_buffer:
            blocks.append({"type": "list", "ordered": list_type == "ordered", "items": list_buffer.copy()})
            list_buffer = []
            list_type = None

    while i < len(lines):
        line = lines[i]

        # 水平線
        if re.match(r'^---+$', line.strip()):
            flush_list()
            blocks.append({"type": "divider"})
            i += 1
            continue

        # 標題
        heading_match = re.match(r'^(#{1,4})\s+(.+)', line)
        if heading_match:
            flush_list()
            level = len(heading_match.group(1))
            text = heading_match.group(2).strip()
            # 移除 anchor id 語法 {#xxx}
            text = re.sub(r'\s*\{#[^}]+\}', '', text).strip()
            blocks.append({"type": "heading", "level": level, "content": text})
            i += 1
            continue

        # 圖片 <img> HTML tag
        img_html_match = re.search(r'<img[^>]+src=["\']([^"\']+)["\'][^>]*alt=["\']([^"\']*)["\']', line)
        if img_html_match:
            flush_list()
            blocks.append({
                "type": "image",
                "url": img_html_match.group(1),
                "alt": img_html_match.group(2),
                "caption": ""
            })
            i += 1
            continue

        # 圖片 Markdown 語法 ![alt](url)
        img_md_match = re.match(r'!\[([^\]]*)\]\(([^)]+)\)', line.strip())
        if img_md_match:
            flush_list()
            blocks.append({
                "type": "image",
                "url": img_md_match.group(2),
                "alt": img_md_match.group(1),
                "caption": ""
            })
            i += 1
            continue

        # 引用 blockquote
        if line.startswith(">"):
            flush_list()
            quote_text = re.sub(r'^>\s*', '', line).strip()
            blocks.append({"type": "quote", "content": quote_text})
            i += 1
            continue

        # 無序列表
        ul_match = re.match(r'^[-*+]\s+(.+)', line)
        if ul_match:
            if list_type != "unordered":
                flush_list()
                list_type = "unordered"
            list_buffer.append(ul_match.group(1).strip())
            i += 1
            continue

        # 有序列表
        ol_match = re.match(r'^\d+\.\s+(.+)', line)
        if ol_match:
            if list_type != "ordered":
                flush_list()
                list_type = "ordered"
            list_buffer.append(ol_match.group(1).strip())
            i += 1
            continue

        # 空行
        if not line.strip():
            flush_list()
            i += 1
            continue

        # 一般段落
        flush_list()
        if line.strip():
            blocks.append({"type": "paragraph", "content": line.strip()})
        i += 1

    flush_list()
    return blocks


def generate_slug(title: str) -> str:
    """從標題產生 URL slug"""
    # 移除特殊字元，轉小寫，空格換連字號
    slug = re.sub(r'[^\w\s-]', '', title.lower())
    slug = re.sub(r'[\s_]+', '-', slug)
    slug = re.sub(r'-+', '-', slug).strip('-')
    return slug or f"article-{datetime.now().strftime('%Y%m%d%H%M%S')}"


# ── Supabase API ──────────────────────────────────────────────────────────────

def upload_draft(article_data: dict) -> Optional[dict]:
    """上傳文章草稿至 Supabase（is_published: false）"""
    url = f"{SUPABASE_URL}/rest/v1/news"
    resp = requests.post(url, headers=SUPABASE_HEADERS, json=article_data)

    if resp.status_code in (200, 201):
        data = resp.json()
        return data[0] if isinstance(data, list) else data
    else:
        print(f"❌ 上傳失敗 [{resp.status_code}]: {resp.text}")
        return None


def publish_article(news_id: str) -> bool:
    """將草稿正式發布（is_published: true）"""
    url = f"{SUPABASE_URL}/rest/v1/news?id=eq.{news_id}"
    payload = {
        "is_published": True,
        "published_at": datetime.now(timezone.utc).isoformat()
    }
    resp = requests.patch(url, headers=SUPABASE_HEADERS, json=payload)
    return resp.status_code in (200, 204)


def check_slug_exists(slug: str) -> Optional[str]:
    """檢查 slug 是否已存在，回傳 id 或 None"""
    url = f"{SUPABASE_URL}/rest/v1/news?slug=eq.{slug}&select=id"
    headers = {**SUPABASE_HEADERS, "Prefer": ""}
    resp = requests.get(url, headers=headers)
    if resp.status_code == 200:
        data = resp.json()
        return data[0]["id"] if data else None
    return None


# ── Preview Token ────────────────────────────────────────────────────────────

def compute_preview_token(slug: str) -> str:
    """計算草稿預覽 HMAC-SHA256 token（前 32 字元），與 preview-article Edge Function 邏輯一致"""
    if not PREVIEW_SECRET:
        return ""
    token = hmac.new(PREVIEW_SECRET.encode(), slug.encode(), hashlib.sha256).hexdigest()
    return token[:32]


def make_preview_url(slug: str) -> str:
    """產生草稿預覽 URL"""
    token = compute_preview_token(slug)
    if not token:
        return f"{RUMA_SITE}/app/admin"  # fallback to admin page
    return f"{RUMA_SITE}/news/{slug}?preview=true&token={token}"


# ── Telegram 通知 ─────────────────────────────────────────────────────────────

def send_telegram(message: str) -> bool:
    """發送 Telegram 訊息給 Eric"""
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": TELEGRAM_CHAT_ID,
        "text": message,
        "parse_mode": "Markdown"
    }
    resp = requests.post(url, json=payload)
    return resp.status_code == 200


# ── 主流程 ────────────────────────────────────────────────────────────────────

def process_article_dir(article_dir: Path) -> Optional[dict]:
    """讀取文章目錄，解析中英文 Markdown，組成 Supabase 格式"""
    zh_file = article_dir / "article_zh-tw.md"
    en_file = article_dir / "article_en.md"

    if not zh_file.exists():
        print(f"❌ 找不到繁中文章：{zh_file}")
        return None

    # 解析繁中文章
    zh_raw = zh_file.read_text(encoding="utf-8")
    zh_meta, zh_body = parse_frontmatter(zh_raw)
    zh_blocks = markdown_to_content_blocks(zh_body)

    # 解析英文文章（可選）
    en_blocks = []
    en_meta = {}
    if en_file.exists():
        en_raw = en_file.read_text(encoding="utf-8")
        en_meta, en_body = parse_frontmatter(en_raw)
        en_blocks = markdown_to_content_blocks(en_body)

    # 組成文章資料
    title = zh_meta.get("title", article_dir.name)
    # 移除標題中的網站名稱後綴（例：" | RUMA 龍舟隊"）
    title = re.sub(r'\s*\|\s*RUMA.*$', '', title).strip()

    # Slug 優先使用 frontmatter 中的值，其次使用目錄名稱（已是 URL-friendly 格式）
    slug = zh_meta.get("slug") or article_dir.name

    cover_image = zh_meta.get("cover_image", "")

    # 從 content blocks 提取第一段作為 excerpt
    excerpt = ""
    for block in zh_blocks:
        if block.get("type") == "paragraph" and block.get("content"):
            excerpt = block["content"][:200]
            break

    excerpt_en = ""
    for block in en_blocks:
        if block.get("type") == "paragraph" and block.get("content"):
            excerpt_en = block["content"][:200]
            break

    return {
        "title": title,
        "title_en": en_meta.get("title", ""),
        "slug": slug,
        "category": zh_meta.get("category", "運動相關"),
        "cover_image": cover_image or None,
        "excerpt": zh_meta.get("excerpt", excerpt),
        "excerpt_en": en_meta.get("excerpt", excerpt_en),
        "content": zh_blocks,
        "content_en": en_blocks,
        "is_pinned": False,
        "pinned_order": 100,
        "is_published": False,
        "published_at": None
    }


def main():
    parser = argparse.ArgumentParser(description="RUMA 文章草稿上傳工具")
    parser.add_argument("--article", type=str, help="文章目錄路徑（相對於 02-Content/）")
    parser.add_argument("--batch", type=str, help="批次上傳目錄（含多篇文章）")
    parser.add_argument("--publish", type=str, help="發布草稿（傳入 news id）")
    parser.add_argument("--dry-run", action="store_true", help="僅解析，不實際上傳")
    args = parser.parse_args()

    # 驗證環境變數
    if not SUPABASE_SERVICE_ROLE_KEY:
        print("❌ 缺少 SUPABASE_SERVICE_ROLE_KEY，請確認 02-Content/.env")
        return

    # ── 發布草稿 ──
    if args.publish:
        print(f"🚀 正在發布文章 ID: {args.publish}")
        if publish_article(args.publish):
            print("✅ 發布成功！")
            send_telegram(
                f"🚀 文章已正式發布（UAT）！\n\n"
                f"🔗 請至 UAT 官網確認：{RUMA_SITE}/news/\n"
                f"📊 GA 將從現在開始追蹤流量表現"
            )
        else:
            print("❌ 發布失敗")
        return

    # ── 單篇上傳 ──
    if args.article:
        article_dirs = [Path(args.article)]
    elif args.batch:
        batch_path = Path(args.batch)
        article_dirs = [d for d in batch_path.iterdir() if d.is_dir()]
    else:
        parser.print_help()
        return

    uploaded = []
    for article_dir in article_dirs:
        print(f"\n📝 處理文章：{article_dir.name}")
        article_data = process_article_dir(article_dir)
        if not article_data:
            continue

        print(f"   標題：{article_data['title']}")
        print(f"   Slug：{article_data['slug']}")
        print(f"   繁中段落數：{len(article_data['content'])}")
        print(f"   英文段落數：{len(article_data['content_en'])}")

        if args.dry_run:
            print("   [Dry Run] 跳過上傳")
            print(f"   預覽 JSON：\n{json.dumps(article_data, ensure_ascii=False, indent=2)[:500]}...")
            continue

        # 檢查 slug 是否已存在
        existing_id = check_slug_exists(article_data["slug"])
        if existing_id:
            print(f"   ⚠️  Slug 已存在（id: {existing_id}），跳過上傳")
            uploaded.append({"id": existing_id, "slug": article_data["slug"], "title": article_data["title"]})
            continue

        result = upload_draft(article_data)
        if result:
            print(f"   ✅ 上傳成功！ID: {result.get('id')}")
            uploaded.append(result)
        else:
            print(f"   ❌ 上傳失敗")

    # ── 發送 Telegram 審核通知 ──
    if uploaded and not args.dry_run:
        article_lines = []
        for a in uploaded:
            title = a.get('title', a.get('slug', 'Unknown'))
            news_id = a.get('id', 'N/A')
            slug = a.get('slug', '')
            preview_url = make_preview_url(slug) if slug else f"{RUMA_SITE}/app/admin"
            article_lines.append(
                f"📌 {title}\n"
                f"   ID: `{news_id}`\n"
                f"   👁 預覽：{preview_url}\n"
                f"   ✅ 發布指令：發布 {news_id}"
            )

        article_list = "\n\n".join(article_lines)
        msg = (
            f"🌐 [UAT] 草稿已上傳至官網（共 {len(uploaded)} 篇）\n\n"
            f"{article_list}\n\n"
            f"❌ 需修改請回覆：修改 {{id}}\n"
            f"📋 查看所有草稿：狀態"
        )
        if send_telegram(msg):
            print(f"\n📱 已發送 Telegram 審核通知給 Eric")
        else:
            print(f"\n⚠️  Telegram 通知發送失敗，請手動通知 Eric")

    print(f"\n✅ 完成！共上傳 {len(uploaded)} 篇文章草稿")


if __name__ == "__main__":
    main()
