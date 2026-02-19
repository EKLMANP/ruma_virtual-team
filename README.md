# RUMA Dragon Boat - 專案總覽

歡迎來到 RUMA 龍舟隊專案！這是一個整合了技術開發、內容行銷、文檔管理的完整專案結構。

---

## 📁 資料夾結構

```
RUMA Dragon Boat/
├── 01-Tech/              # 技術開發部門
├── 02-Content/           # 內容行銷部門
├── 03-Docs/              # 文檔資料部門
└── 04-Archive/           # 歷史備份部門
```

---

## 🎯 各部門說明

### 01-Tech/ - 技術開發部門
包含所有技術開發相關的內容：
- **website/** - RUMA 官方網站專案 (React + Vite + Supabase)
- **.ai-agents/** - AI 工具配置（適用於 Claude Code、Antigravity 等）

👉 [查看技術部門詳情](./01-Tech/README.md)

### 02-Content/ - 內容行銷部門
包含所有內容創作和媒體資源：
- **articles/** - 龍舟相關文章（中英雙語）
- **assets/** - 圖片、Logo 等共用資源

👉 [查看內容部門詳情](./02-Content/README.md)

### 03-Docs/ - 文檔資料部門
包含所有文檔和手冊：
- **development/** - 開發文檔、架構說明
- **user-manuals/** - 用戶使用手冊

👉 [查看文檔部門詳情](./03-Docs/README.md)

### 04-Archive/ - 歷史備份部門
包含歷史資料和已棄用的文件：
- **old-migrations/** - 舊版資料庫遷移記錄
- **deprecated/** - 已棄用的文件

---

## 🤝 AI 工具整合

本專案結構設計為與多種 AI 工具協同工作：

### Claude Code
- 使用 `01-Tech/.ai-agents/` 中的技能配置
- 專注於技術開發和程式碼優化

### Antigravity (或其他 AI 工具)
- 同樣使用 `01-Tech/.ai-agents/` 中的技能配置
- 可專注於內容創作、文檔撰寫等任務

### 避免衝突的設計原則
1. **統一配置位置** - 所有 AI 工具共用 `.ai-agents/` 資料夾
2. **明確的部門分工** - 技術、內容、文檔分離
3. **清晰的命名規則** - 使用數字前綴確保排序一致
4. **完整的文檔** - 每個部門都有 README 說明用途

---

## 🚀 快速開始

### 技術開發
```bash
cd "01-Tech/website"
npm install
npm run dev
```

### 內容創作
查看 `02-Content/articles/` 中的文章模板和範例

### 查看文檔
查看 `03-Docs/` 中的完整文檔索引

---

## 📝 更新日誌

### 2026-02-17
- ✨ 整合原有 `RUMA` 和 `ruma` 資料夾
- 🏗️ 建立清晰的部門結構
- 🤖 統一 AI 工具配置位置
- 📚 創建完整的 README 文檔系統

---

## 👥 團隊

RUMA Dragon Boat Team

---

**最後更新：** 2026-02-17
