# 02-Content - 內容行銷部門

這個資料夾包含 RUMA 龍舟隊的所有內容創作、Agent Skills 和媒體資源。

---

## 📁 資料夾結構

```
02-Content/
├── ruma-seo-master/          # 🔍 SEO/AEO/GEO Master Agent Skill
│   ├── SKILL.md
│   └── resources/
│       ├── seo_aeo_geo_guide.md
│       └── keyword_library.md
├── ruma-content-alchemist/   # ✍️ Content Alchemist Agent Skill
│   ├── SKILL.md
│   └── templates/
│       ├── article_zh-tw_template.md
│       └── article_en_template.md
├── ruma-creative-master/     # 🎨 Creative Master Agent Skill
│   ├── SKILL.md
│   └── resources/
│       ├── image_prompt_guide.md
│       └── api_integration_guide.md
├── articles/                 # 📝 已產出的龍舟文章
│   ├── dragon-boat-beginner-guide/
│   ├── dragon-boat-muscle-groups/
│   ├── dragon-boat-muscle-soreness/
│   └── dragon-boat-race-guide/
├── assets/                   # 🖼 共用媒體資源
└── .env                      # 🔑 API Keys（不進 Git）
```

---

## 🤖 RUMA 官網文章自動化發布流程

> **設計原則**：人工介入愈少愈好，但每個關鍵節點都有 Eric 作為審核檢核點。每次人工修改後，各 Agent Skill 會學習調整風格、口吻、用字遣詞，讓產出的文章專業但有趣，同時符合真人寫作口吻與 RUMA 品牌調性。

### 🗓 每週自動化排程

```
每週五 08:00
     │
     ▼
┌─────────────────────────────────────────────────────────────────┐
│ Step 1 │ 🔍 SEO/AEO/GEO Master 自動啟動                        │
│         │ → 關鍵字研究（SEO + AEO + GEO）                       │
│         │ → 產出 30 個高流量低競爭關鍵字詞組                    │
│         │ → 綜合評估後提供 3 個文章框架                         │
└─────────────────────────────────────────────────────────────────┘
     │
     ▼
┌─────────────────────────────────────────────────────────────────┐
│ Step 2 │ ✍️ Content Alchemist 接收框架 & 關鍵字                 │
│         │ → 全球資料蒐集（Reddit、YouTube、IDBF 等）             │
│         │ → 撰寫 3 篇繁中 + 英文文章草稿 v1                     │
│         │ → 自我審閱（30年行銷寫手角度）                        │
│         │ → 產出每篇文章的圖片 Prompt                           │
└─────────────────────────────────────────────────────────────────┘
     │
     ▼
┌─────────────────────────────────────────────────────────────────┐
│ Step 3 │ 🎨 Creative Master 接收文章草稿 v1 × 3                 │
│         │ → 呼叫 Gemini API 產出封面圖 + 段落配圖               │
│         │ → 上傳圖片至 imgBB                                    │
│         │ → 嵌入圖片 URL 至中英文文章                           │
└─────────────────────────────────────────────────────────────────┘
     │
     ▼
┌─────────────────────────────────────────────────────────────────┐
│ Step 4 │ 📱 Telegram 通知 Eric 審核（第一次人工介入）            │
│         │ → 傳送 3 篇完整文章（含圖）供審核                     │
│         │ → Eric 審核文章內容 + 視覺設計                        │
│         │ → 回覆 ✅ 通過 或 ❌ 需修改（附修改意見）              │
└─────────────────────────────────────────────────────────────────┘
     │
     ├──── ❌ 需修改 ────► Agent 學習修改意見 → 重新產出 → 再次通知
     │
     ▼ ✅ 通過
┌─────────────────────────────────────────────────────────────────┐
│ Step 5 │ 🌐 自動上傳至 rumadragonboat.com 儲存為草稿 v2         │
│         │ → 透過 API 上傳至官網 CMS                             │
│         │ → 儲存為「草稿」狀態（尚未公開發布）                  │
│         │ → Telegram 通知 Eric 進行最終審核（第二次人工介入）    │
└─────────────────────────────────────────────────────────────────┘
     │
     ├──── ❌ 需修改 ────► Eric 直接在 CMS 修改 → 通知 Agent 學習
     │
     ▼ ✅ 通過
┌─────────────────────────────────────────────────────────────────┐
│ Step 6 │ 🚀 正式發布至 https://rumadragonboat.com/news          │
│         │ → 嵌入 Google Tag Manager（流量追蹤）                 │
│         │ → 社群推廣素材（IG/FB 摘要圖卡）                      │
└─────────────────────────────────────────────────────────────────┘
     │
     ▼
┌─────────────────────────────────────────────────────────────────┐
│ Step 7 │ 📊 Google Analytics 定期追蹤成效                       │
│         │ → 流量、停留時間、跳出率                              │
│         │ → 關鍵字排名變化                                      │
│         │ → 每月成效報告                                        │
└─────────────────────────────────────────────────────────────────┘
```

---

### 🔄 Agent 學習回饋機制

每次 Eric 審核並修改後，各 Agent Skill 會自動學習：

| 學習項目 | 說明 |
|---------|------|
| **風格調整** | 記錄 Eric 修改的用字遣詞、語氣偏好 |
| **口吻校正** | 確保文章更貼近真人寫作 & RUMA 品牌調性 |
| **視覺偏好** | 記錄 Eric 對圖片風格的修改意見 |
| **SEO 優化** | 根據 GA 成效數據調整關鍵字策略 |

---

### 📋 各 Agent Skill 職責

| Skill | 職責 | 輸入 | 輸出 |
|-------|------|------|------|
| **🔍 SEO/AEO/GEO Master** | 策略研究 & 框架產出 | 自動觸發（每週五 8:00） | 30 個關鍵字 + 3 個文章框架 |
| **✍️ Content Alchemist** | 資料蒐集 & 撰寫文章 | 關鍵字 + 框架 | 3 篇中英文文章草稿 v1 + 圖片 Prompt |
| **🎨 Creative Master** | 產圖 + 通知 + 發布 | 文章草稿 v1 + Prompt | 完整文章（含圖）→ Telegram 通知 → 草稿 v2 → 發布 |

---

### 🔑 API 整合

| 服務 | 用途 | 環境變數 |
|------|------|---------|
| Google AI Studio (Gemini) | 圖片生成 | `GOOGLE_AI_STUDIO_API_KEY` |
| imgBB | 圖片 Hosting | `IMGBB_API_KEY` |
| Telegram Bot | 審核通知 | `TELEGRAM_BOT_TOKEN` / `TELEGRAM_CHAT_ID` |
| RUMA 官網 CMS API | 草稿上傳 & 發布 | 待確認（見備註） |
| Google Tag Manager | 流量追蹤 | 嵌入官網 |

> **備註**：RUMA 官網「建立最新消息」功能需設計成可透過 API 直接上傳並儲存為草稿 v2，Eric 透過 Telegram bot 審核通過後直接觸發發布。具體 API 端點待 01-Tech 確認後補充至 `ruma-creative-master/resources/api_integration_guide.md`。

---

### 📱 Telegram 審核流程

**第一次審核（草稿 v1 完成後）：**
```
Bot 訊息：
📝 新文章待審核（3篇）

📌 文章1：[標題]
📌 文章2：[標題]
📌 文章3：[標題]

請審核文章內容 & 視覺設計
✅ 回覆「通過」→ 上傳草稿 v2
❌ 回覆「修改：[修改意見]」→ 重新產出
```

**第二次審核（草稿 v2 上傳後）：**
```
Bot 訊息：
🌐 草稿已上傳至官網

📌 預覽連結：https://rumadragonboat.com/news/[slug]（草稿模式）

✅ 回覆「發布」→ 正式發布
❌ 回覆「修改：[修改意見]」→ 返回修改
```

---

## 📝 Articles - 已產出文章

### 文章結構

每篇文章包含：
```
article-name/
├── article_zh-tw.md      # 繁體中文版本（已嵌入圖片）
├── article_en.md         # 英文版本（已嵌入圖片）
├── image_prompts.md      # 圖片生成提示詞（備查）
├── cover.jpg             # 封面圖片
├── p1.jpg, p2.jpg...     # 內文圖片
└── social/               # 社群推廣素材
    ├── ig_card.jpg
    └── social_copy.md
```

---

## 📋 內容規範

- ✅ 台灣用語（避免中國用語）
- ✅ 專業但有趣的口吻，貼近真人寫作
- ✅ 中英文版本各自撰寫（非逐字翻譯）
- ✅ 符合 RUMA 品牌調性

詳細規範：
- SEO/AEO/GEO 指南：`ruma-seo-master/resources/seo_aeo_geo_guide.md`
- 關鍵字庫：`ruma-seo-master/resources/keyword_library.md`
- 圖片 Prompt 指南：`ruma-creative-master/resources/image_prompt_guide.md`
- API 整合指南：`ruma-creative-master/resources/api_integration_guide.md`

---

## 📚 相關文檔

- [專案總覽](../README.md)
- [技術部門](../01-Tech/README.md)
- [文檔部門](../03-Docs/README.md)

---

**最後更新：** 2026-02-18
