# RUMA 虛擬團隊 — 跨角色自動化工作流程

> **最後更新：** 2026-02-18
> **適用範圍：** 02-Content 部門所有 AI 角色

---

## 工作流程 A：每週內容行銷自動化流程

**觸發條件：** 每週五 08:00 自動啟動（無需人工介入）

```
┌─────────────────────────────────────────────────────────┐
│  每週五 08:00 自動觸發                                   │
└──────────────────────┬──────────────────────────────────┘
                       │
                       ▼
┌─────────────────────────────────────────────────────────┐
│  Step 1：RUMA_SEO_Master                                │
│  詳細流程：ruma-seo-master/SKILL.md                     │
│                                                         │
│  產出：                                                  │
│  • 30 個高流量低競爭關鍵字詞組（繁中 + 英文）             │
│  • 3 個文章框架（完整 H1-H3 + Schema + 競品分析）        │
└──────────────────────┬──────────────────────────────────┘
                       │
                       ▼
┌─────────────────────────────────────────────────────────┐
│  Step 2：RUMA_Content_Alchemist                         │
│  詳細流程：ruma-content-alchemist/SKILL.md              │
│                                                         │
│  輸入：Step 1 的 30 個關鍵字 + 3 個框架                  │
│  產出：                                                  │
│  • articles/[slug]/article_zh-tw.md                    │
│  • articles/[slug]/article_en.md                       │
│  • articles/[slug]/image_prompts.md                    │
└──────────────────────┬──────────────────────────────────┘
                       │
                       ▼
┌─────────────────────────────────────────────────────────┐
│  Step 3：RUMA_Visual_Design_Master                      │
│  詳細流程：ruma-creative-master/SKILL.md                │
│                                                         │
│  輸入：Step 2 的文章草稿 + image_prompts.md             │
│  執行：                                                  │
│  1. 呼叫 Gemini API 產圖（每篇 4-5 張）                  │
│  2. 上傳至 imgBB（SEO 友善檔名）                         │
│  3. 將圖片 URL 嵌入繁中 + 英文文章                       │
│                                                         │
│  產出：完整圖文版文章（草稿 v1）                          │
└──────────────────────┬──────────────────────────────────┘
                       │
                       ▼
┌─────────────────────────────────────────────────────────┐
│  Step 4：RUMA_Head 第一階段審核                          │
│  詳細流程：ruma-head/SKILL.md（流程 A）                  │
│                                                         │
│  審核面向：讀者價值、品牌調性、知識含金量、視覺質感、       │
│           行銷效果、SEO 合規                              │
│                                                         │
│  ✅ 通過 → Telegram 通知 Eric（附審核報告）               │
│  ❌ 不通過 → 退回對應角色重做（附具體修改意見）            │
└──────────────────────┬──────────────────────────────────┘
                       │ [Eric 收到通知]
                       ▼
┌─────────────────────────────────────────────────────────┐
│  Eric 第一次確認（Telegram 回覆）                        │
│                                                         │
│  ✅ 回覆「通過」→ Step 5                                 │
│  ❌ 回覆「修改：[意見]」→ 退回 RUMA_Head 重新審核         │
└──────────────────────┬──────────────────────────────────┘
                       │
                       ▼
┌─────────────────────────────────────────────────────────┐
│  Step 5：RUMA_Visual_Design_Master 上傳草稿              │
│                                                         │
│  執行：                                                  │
│  • 呼叫 Supabase API 上傳文章（is_published: false）     │
│  • 草稿網址：https://rumadragonboat.com/news/[slug]      │
│                                                         │
│  Telegram 通知 Eric：                                    │
│  「草稿已上傳，請至以下連結預覽：[URL]                   │
│   回覆「發布」→ 正式公開                                  │
│   回覆「修改：[意見]」→ 返回修改」                        │
└──────────────────────┬──────────────────────────────────┘
                       │ [Eric 預覽後]
                       ▼
┌─────────────────────────────────────────────────────────┐
│  Eric 第二次確認（Telegram 回覆）                        │
│                                                         │
│  ✅ 回覆「發布」→ Step 6                                 │
│  ❌ 回覆「修改：[意見]」→ 退回修改                        │
└──────────────────────┬──────────────────────────────────┘
                       │
                       ▼
┌─────────────────────────────────────────────────────────┐
│  Step 6：正式發布 + GTM 追蹤                             │
│                                                         │
│  執行：                                                  │
│  • 更新 Supabase：is_published: true                    │
│  • 確認 GTM（GTM-T3P8NN9J）已嵌入文章頁面               │
│  • GA4（G-Y3SNWN0XG7）開始追蹤流量                      │
│  • Telegram 通知 Eric 發布完成                           │
│                                                         │
│  最終交付結構：                                          │
│  articles/[slug]/                                       │
│  ├── article_zh-tw.md   # 已嵌入圖片的繁中版            │
│  ├── article_en.md      # 已嵌入圖片的英文版             │
│  ├── image_prompts.md   # 圖片 Prompt（備查）            │
│  ├── cover.jpg          # 封面圖                        │
│  ├── p1.jpg, p2.jpg...  # 段落配圖                      │
│  └── social/            # 社群素材（Optional）           │
│      ├── ig_card.jpg                                    │
│      └── social_copy.md                                 │
└─────────────────────────────────────────────────────────┘
```

---

## 工作流程 B：訓練計劃規劃流程

**觸發條件：** 距龍舟比賽 N 週前由 Eric 指定，或 Eric 直接指派

```
┌─────────────────────────────────────────────────────────┐
│  觸發：Eric 指定備賽目標                                  │
│  例：「端午節龍舟賽還有 8 週，請規劃訓練計劃」             │
└──────────────────────┬──────────────────────────────────┘
                       │
                       ▼
┌─────────────────────────────────────────────────────────┐
│  Step 1：RUMA_Head_of_Training 評估 + 規劃               │
│  詳細流程：ruma-head-of-training/SKILL.md               │
│                                                         │
│  評估：備賽週數、比賽距離、隊員體能、訓練頻率             │
│  規劃：                                                  │
│  • 划龍舟訓練課表（水上）                                 │
│  • 重量訓練課表（健身房）                                 │
│  • 心肺訓練課表（戶外）                                   │
│  • 週訓練總排程                                          │
└──────────────────────┬──────────────────────────────────┘
                       │
                       ▼
┌─────────────────────────────────────────────────────────┐
│  Step 2：RUMA_Head 審核訓練計劃                          │
│  詳細流程：ruma-head/SKILL.md（流程 B）                  │
│                                                         │
│  審核面向：備賽合理性、難度漸進、全員適用性、              │
│           目標導向、實際可執行性                          │
│                                                         │
│  ✅ 通過 → 提交 Eric 確認                                │
│  ❌ 不通過 → 退回 RUMA_Head_of_Training 調整             │
└──────────────────────┬──────────────────────────────────┘
                       │ [Eric 收到提交]
                       ▼
┌─────────────────────────────────────────────────────────┐
│  Eric 確認訓練計劃                                       │
│                                                         │
│  ✅ 確認 → Step 3                                        │
│  ❌ 修改 → 退回調整                                      │
└──────────────────────┬──────────────────────────────────┘
                       │
                       ▼
┌─────────────────────────────────────────────────────────┐
│  Step 3：發送訓練計劃給隊員                               │
│                                                         │
│  執行：                                                  │
│  • 上傳訓練計劃至 Google Drive                           │
│  • 透過 LINE Official Account 發送通知給隊員             │
│  • 訓練計劃保存至 NotebookLM 知識庫                      │
└─────────────────────────────────────────────────────────┘
```

---

## 共用工具與 API 存取清單

| 服務 | 用途 | 可存取角色 | 設定位置 |
|------|------|---------|---------|
| **Google Drive** | 文件儲存與共享 | 訓練長、設計師、寫手、SEO | [連結](https://drive.google.com/drive/folders/1Prd606WBGn7LQuYFfWfLp4ObjHgZq9Do) |
| **LINE Official Account** | 通知隊員 | 訓練長、設計師、寫手、SEO | 需 Eric 授權 |
| **Gemini / Google AI Studio** | AI 產圖、AI 輔助 | 全員 | `API_KEY` 見 `.env` |
| **NotebookLM** | 知識庫建立 | 全員 | Google 帳號登入 |
| **Telegram Bot** | 通知 Eric 審核 | 設計師（Visual Design Master）| `TELEGRAM_BOT_TOKEN` 見 `.env` |
| **imgBB** | 圖片 hosting | 設計師（Visual Design Master）| `IMGBB_API_KEY` 見 `.env` |
| **Supabase** | 官網 CMS 資料庫 | 設計師（Visual Design Master）| `SUPABASE_SERVICE_ROLE_KEY` 見 `.env` |
| **Google Analytics / GTM** | 流量追蹤 | SEO Master（追蹤報告）| GTM-T3P8NN9J / G-Y3SNWN0XG7 |
| **rumadragonboat@gmail.com** | 團隊對外聯絡 | 全員 | Gmail |

### API Keys 位置

```
/Users/ericpan/RUMA Dragon Boat/02-Content/.env
```

---

## 角色觸發條件彙整

| 角色 | 觸發條件 | 觸發方式 |
|------|---------|---------|
| RUMA_SEO_Master | 每週五 08:00 | 自動排程 |
| RUMA_Content_Alchemist | SEO Master 完成後 | 自動接力 |
| RUMA_Visual_Design_Master | Content Alchemist 完成後 | 自動接力 |
| RUMA_Head | 任一成員完成交付後 | 自動審核 |
| RUMA_Head_of_Training | Eric 指派備賽任務時 | 人工指定 |

---

## 各角色詳細 SKILL.md 位置

| 角色 | SKILL.md 路徑 |
|------|-------------|
| RUMA_Head（主管）| `02-Content/ruma-head/SKILL.md` |
| RUMA_Head_of_Training（訓練長）| `02-Content/ruma-head-of-training/SKILL.md` |
| RUMA_Visual_Design_Master（設計師）| `02-Content/ruma-creative-master/SKILL.md` |
| RUMA_Content_Alchemist（內容寫手）| `02-Content/ruma-content-alchemist/SKILL.md` |
| RUMA_SEO_Master（SEO 專家）| `02-Content/ruma-seo-master/SKILL.md` |
