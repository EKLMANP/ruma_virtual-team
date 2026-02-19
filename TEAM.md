# RUMA 龍舟隊 — 虛擬 AI 團隊總覽

> **團隊 Email：** rumadragonboat@gmail.com
> **官網：** https://rumadragonboat.com
> **Instagram：** https://www.instagram.com/ruma_dragonboat/
> **訓練場地：** 台灣新北市新店區碧潭

---

## 關於 RUMA

RUMA 是 2024 年成立的台灣龍舟隊，成員來自台灣、馬來西亞、菲律賓、印尼、巴西、阿根廷、美國，熱愛各式運動，希望透過龍舟運動保持身體健康。

**隊伍名稱意涵：**
- **R** — Rebel（叛逆）
- **U** — Unity（團結）
- **M** — Mawtux（勇敢 / Bravery in Tayal language）
- **A** — Amistad（友誼 / Friendship in Spanish）
- **RUMA** — 馬來文「家」（Home in Malay）

**核心價值：**
| 價值觀 | 說明 |
|-------|------|
| Team work matters | 團隊至上 |
| Sharing is caring | 樂於分享 |
| Growth mindset | 成長心態 |
| Transparent & open-minded | 透明開放 |

---

## 2026 團隊目標

1. **招募新成員**：透過部落格內容行銷、社群行銷吸引更多新朋友加入
2. **爭取贊助**：吸引潛在贊助商提供金錢或商品贊助
3. **海外邀賽**：收到更多海外龍舟比賽主辦單位邀請
4. **賽場成績**：端午節龍舟賽進前 5 名

---

## 組織架構

```
Eric（最終決策者）
  │
  └── RUMA_Head（團隊主管）
        │
        ├── RUMA_Head_of_Training（訓練長）
        │
        ├── RUMA_Visual_Design_Master（設計師）
        │     → 詳細職責：02-Content/ruma-creative-master/SKILL.md
        │
        ├── RUMA_Content_Alchemist（內容行銷寫手）
        │     → 詳細職責：02-Content/ruma-content-alchemist/SKILL.md
        │
        └── RUMA_SEO_Master（SEO/AEO/GEO 專家）
              → 詳細職責：02-Content/ruma-seo-master/SKILL.md
```

---

## 五大角色一覽

| 角色 | 代號 | 核心職責 | 輸入 | 輸出 |
|------|------|---------|------|------|
| 團隊主管 | RUMA_Head | 審核所有成員交付物，通過後提交 Eric | 各成員產出 | 審核結果 + Telegram 通知 Eric |
| 訓練長 | RUMA_Head_of_Training | 規劃划龍舟、重訓、心肺訓練課表 | 備賽目標 + 賽事時程 | 訓練課表（→ RUMA_Head 審核）|
| 設計師 | RUMA_Visual_Design_Master | 產圖、上傳、嵌入文章、發布網站 | 文章草稿 + image_prompts.md | 完整圖文文章 + 發布至官網 |
| 內容行銷寫手 | RUMA_Content_Alchemist | 研究資料、撰寫繁中 + 英文文章 | SEO 關鍵字框架 | 3 篇雙語文章 + 圖片 Prompt |
| SEO/AEO/GEO 專家 | RUMA_SEO_Master | 關鍵字研究、文章框架、競品分析 | 無（自動觸發）| 30 個關鍵字 + 3 個文章框架 |

---

## 工具與 API 存取權限

| 服務 | 用途 | 可存取角色 |
|------|------|---------|
| Google Drive | 文件儲存與共享 | 訓練長、設計師、寫手、SEO |
| LINE Official Account | 通知隊員 | 訓練長、設計師、寫手、SEO |
| Gemini / Google AI Studio | AI 產圖、AI 輔助 | 全員 |
| NotebookLM | 知識庫建立 | 全員 |
| Telegram Bot | 通知 Eric 審核 | 設計師（Visual Design Master）|
| imgBB | 圖片 hosting | 設計師（Visual Design Master）|
| Supabase | 官網 CMS 資料庫 | 設計師（Visual Design Master）|
| Google Analytics / GTM | 流量追蹤分析 | SEO Master |
| rumadragonboat@gmail.com | 團隊對外聯絡 | 全員 |

---

## 自動化工作流程

詳細流程請見：`02-Content/WORKFLOW.md`

**兩條主要流程：**
1. **每週內容行銷流程**（每週五 08:00 自動觸發）：SEO Master → Content Alchemist → Visual Design Master → RUMA_Head 審核 → Eric 確認 → 發布
2. **訓練計劃規劃流程**（依賽事時程觸發）：Head of Training → RUMA_Head 審核 → Eric 確認 → 發送隊員

---

## 各角色 SKILL.md 檔案位置

| 角色 | SKILL.md 路徑 |
|------|-------------|
| RUMA_Head（主管）| `02-Content/ruma-head/SKILL.md` |
| RUMA_Head_of_Training（訓練長）| `02-Content/ruma-head-of-training/SKILL.md` |
| RUMA_Visual_Design_Master（設計師）| `02-Content/ruma-creative-master/SKILL.md` |
| RUMA_Content_Alchemist（內容寫手）| `02-Content/ruma-content-alchemist/SKILL.md` |
| RUMA_SEO_Master（SEO 專家）| `02-Content/ruma-seo-master/SKILL.md` |
