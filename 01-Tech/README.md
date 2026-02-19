# 01-Tech - 技術開發部門

這個資料夾包含 RUMA 龍舟隊的所有技術開發相關內容。

---

## 📁 資料夾結構

```
01-Tech/
├── website/              # 主網站專案
└── .ai-agents/           # AI 工具配置
```

---

## 🌐 Website - 主網站專案

RUMA 龍舟隊官方網站，使用現代化的技術棧：

### 技術架構
- **Frontend**: React 19 + Vite
- **Backend**: Supabase (BaaS)
- **Styling**: Tailwind CSS
- **Hosting**: Vercel
- **Database**: PostgreSQL with Row Level Security (RLS)

### 快速開始
```bash
cd website
npm install
npm run dev
```

### 環境配置
- **UAT (測試環境)**: `develop` 分支
- **Production (正式環境)**: `main` 分支

詳細的開發流程和部署說明請參考：
👉 [website/README.md](./website/README.md)

---

## 🤖 .ai-agents/ - AI 工具配置

統一的 AI 代理技能配置資料夾，適用於所有 AI 開發工具。

### 可用的技能

#### 網站開發相關
- **performance-expert/** - 性能優化專家
- **security-expert/** - 安全性專家
- **ruma-growth-architect/** - 成長架構師

#### 內容創作相關
- **ruma-article-writer/** - 文章撰寫專家
  - 支援中英雙語文章創作
  - 包含 SEO/AEO 優化指南
  - 提供圖片提示詞指南

### 使用方式

#### Claude Code
```bash
# Claude Code 會自動識別 .ai-agents/ 資料夾中的技能
# 在專案根目錄執行即可
claude code
```

#### Antigravity (或其他 AI 工具)
```bash
# 確保 AI 工具配置指向此資料夾
# 在 AI 工具設置中指定技能路徑：
# /path/to/RUMA Dragon Boat/01-Tech/.ai-agents/
```

### 新增自訂技能

如需新增專案特定的技能：

1. 在 `.ai-agents/` 資料夾中創建新的技能目錄
2. 參考現有技能的結構創建 `SKILL.md`
3. 定義技能的觸發條件和指令
4. 所有 AI 工具會自動識別新技能

---

## 🔧 開發最佳實踐

### 代碼品質
- ✅ 使用 ESLint 進行代碼檢查
- ✅ 遵循 React 最佳實踐
- ✅ 保持組件小而專注

### 安全性
- 🔒 所有資料表必須啟用 RLS
- 🔒 前端永不驗證權限（僅 UI 控制）
- 🔒 敏感資訊使用環境變數

### 性能優化
- ⚡ 使用 Code Splitting
- ⚡ 優化圖片格式（WebP）
- ⚡ 實施適當的快取策略

詳細的架構最佳實踐請參考：
👉 [website/ARCHITECTURE_BEST_PRACTICES.md](./website/ARCHITECTURE_BEST_PRACTICES.md)

---

## 📚 相關文檔

- [專案總覽](../README.md)
- [內容部門](../02-Content/README.md)
- [文檔部門](../03-Docs/README.md)

---

**最後更新：** 2026-02-17
