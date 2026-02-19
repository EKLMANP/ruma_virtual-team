# RUMA 官網 CMS API 整合指南

> **確認日期**：2026-02-18  
> **確認結果**：RUMA 官網使用 **Supabase** 作為後端資料庫，透過 Supabase REST API 直接操作 `news` 資料表即可上傳文章草稿。

---

## 1. 技術架構確認

| 項目 | 技術 |
|------|------|
| **前端框架** | Vite + React |
| **後端/資料庫** | Supabase (PostgreSQL) |
| **部署平台** | Vercel |
| **CMS 類型** | Supabase 直接操作（無獨立 CMS） |
| **GTM 容器 ID** | `GTM-T3P8NN9J` |
| **GA Measurement ID** | `G-Y3SNWN0XG7` |

---

## 2. Supabase 連線資訊

```env
SUPABASE_URL=https://tmhlxhkzmssqnptmqzhy.supabase.co
SUPABASE_ANON_KEY=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...  # 見 01-Tech/website/.env
SUPABASE_SERVICE_ROLE_KEY=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...  # 見 01-Tech/website/.env
```

> ⚠️ **注意**：上傳草稿需使用 `SUPABASE_SERVICE_ROLE_KEY`（繞過 RLS 權限），不可使用 `ANON_KEY`。

---

## 3. `news` 資料表結構

| 欄位 | 類型 | 說明 |
|------|------|------|
| `id` | uuid | 主鍵（自動產生） |
| `title` | text | 繁體中文標題 |
| `title_en` | text | 英文標題 |
| `slug` | text | URL 路徑（唯一，例：`dragon-boat-beginner-guide`） |
| `category` | text | 分類（見下方分類清單） |
| `cover_image` | text | 封面圖片 URL（imgBB URL） |
| `excerpt` | text | 繁中摘要（150-160 字） |
| `excerpt_en` | text | 英文摘要 |
| `content` | jsonb | 繁中正文（JSON 陣列，見格式說明） |
| `content_en` | jsonb | 英文正文（JSON 陣列） |
| `is_pinned` | boolean | 是否置頂（預設 false） |
| `pinned_order` | integer | 置頂排序（預設 100） |
| `is_published` | boolean | **`false` = 草稿，`true` = 已發布** |
| `published_at` | timestamptz | 發布時間（草稿時為 null） |
| `author_id` | uuid | 作者 ID（可為 null） |
| `created_at` | timestamptz | 建立時間（自動） |
| `updated_at` | timestamptz | 更新時間（自動） |

### 分類清單

```
體驗招募 / 比賽消息 / 團隊活動 / 運動相關 / 其他
```

### `content` JSON 格式

`content` 和 `content_en` 欄位為 JSON 陣列，每個元素代表一個內容區塊：

```json
[
  {
    "type": "paragraph",
    "content": "這是一段正文內容..."
  },
  {
    "type": "heading",
    "level": 2,
    "content": "## H2 標題"
  },
  {
    "type": "image",
    "url": "https://i.ibb.co/xxxxx/image.jpg",
    "alt": "圖片描述",
    "caption": "圖片說明"
  },
  {
    "type": "list",
    "items": ["項目一", "項目二", "項目三"]
  }
]
```

---

## 4. API 端點

### 4.1 上傳草稿 v2（POST）

```
POST https://tmhlxhkzmssqnptmqzhy.supabase.co/rest/v1/news
```

**Headers：**
```
Content-Type: application/json
apikey: {SUPABASE_SERVICE_ROLE_KEY}
Authorization: Bearer {SUPABASE_SERVICE_ROLE_KEY}
Prefer: return=representation
```

**Body（草稿，`is_published: false`）：**
```json
{
  "title": "龍舟新手完整入門指南",
  "title_en": "Complete Dragon Boat Beginner Guide",
  "slug": "dragon-boat-beginner-guide",
  "category": "運動相關",
  "cover_image": "https://i.ibb.co/xxxxx/cover.jpg",
  "excerpt": "第一次划龍舟不知道怎麼開始？...",
  "excerpt_en": "First time dragon boating and don't know where to start?...",
  "content": [...],
  "content_en": [...],
  "is_pinned": false,
  "pinned_order": 100,
  "is_published": false,
  "published_at": null
}
```

**成功回應（201）：**
```json
[{ "id": "uuid-xxxx", "slug": "dragon-boat-beginner-guide", ... }]
```

---

### 4.2 正式發布（PATCH）

Eric 在 Telegram 回覆「發布」後，將草稿狀態改為已發布：

```
PATCH https://tmhlxhkzmssqnptmqzhy.supabase.co/rest/v1/news?id=eq.{news_id}
```

**Headers：**（同上）

**Body：**
```json
{
  "is_published": true,
  "published_at": "2026-02-18T09:00:00+08:00"
}
```

---

### 4.3 查詢草稿（GET）

確認草稿是否成功上傳：

```
GET https://tmhlxhkzmssqnptmqzhy.supabase.co/rest/v1/news?slug=eq.{slug}&select=id,title,is_published
```

---

## 5. 自動上傳腳本

腳本位置：`02-Content/ruma-creative-master/resources/upload_draft.py`

### 使用方式

```bash
# 上傳單篇草稿
python upload_draft.py --article articles/dragon-boat-beginner-guide

# 上傳本週 3 篇草稿
python upload_draft.py --batch articles/week-2026-02-18/

# 發布已上傳的草稿
python upload_draft.py --publish {news_id}
```

### 腳本功能

1. 讀取 `article_zh-tw.md` 和 `article_en.md`
2. 解析 Markdown 轉換為 Supabase `content` JSON 格式
3. 上傳至 Supabase `news` 資料表（`is_published: false`）
4. 回傳草稿預覽 URL：`https://rumadragonboat.com/news/{slug}`
5. 透過 Telegram Bot 發送第二階段審核通知

---

## 6. 草稿預覽 URL

> ⚠️ **注意**：目前官網前台 `fetchNewsDetail` 只查詢 `is_published = true` 的文章，草稿無法直接預覽。

**解決方案（待 01-Tech 實作）**：
- 方案 A：在 URL 加入 `?preview=true&token={secret}` 參數，後台驗證 token 後顯示草稿
- 方案 B：使用 Supabase Admin 後台直接預覽
- 方案 C（暫用）：Eric 直接登入 RUMA 後台管理頁面（`/admin`）查看草稿

---

## 7. Telegram 審核流程整合

### 第一階段（草稿 v1 完成後）
```
Creative Master → 產圖完成 → 發送 Telegram 通知（含 3 篇文章附件）
Eric 回覆「通過」→ 觸發 upload_draft.py
```

### 第二階段（草稿 v2 上傳後）
```
upload_draft.py 上傳成功 → 發送 Telegram 通知（含後台管理連結）
Eric 回覆「發布」→ 觸發 PATCH API 將 is_published 改為 true
```

### Telegram Bot 設定
```env
TELEGRAM_BOT_TOKEN=7923496984:AAH8H6Y5ZslKT9l0UVWitUZC6WXiHovdlM4
TELEGRAM_CHAT_ID=882308403
```

---

## 8. GTM 追蹤確認

GTM 已嵌入官網（`GTM-T3P8NN9J`），文章發布後自動追蹤：

- **頁面瀏覽**：`page_view` 事件（自動）
- **文章閱讀**：可在 GTM 設定 scroll depth trigger
- **CTA 點擊**：可追蹤「立即報名」等按鈕點擊

GA4 Measurement ID：`G-Y3SNWN0XG7`

---

## 9. 待確認事項

| 項目 | 狀態 | 負責人 |
|------|------|--------|
| Supabase Service Role Key 加入 `02-Content/.env` | ✅ 已確認 | Eric |
| 草稿預覽功能實作（方案 A/B/C） | ⏳ 待決定 | 01-Tech |
| Telegram Bot Webhook 設定（接收 Eric 回覆） | ⏳ 待實作 | 01-Tech |
| `upload_draft.py` 腳本測試 | ⏳ 待測試 | Creative Master |
