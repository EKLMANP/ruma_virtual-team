# Claude.ai Project 設定指南（手機 APP 用）

> 完成以下步驟後，你可以在 **手機 Claude APP** 直接切換 RUMA 虛擬團隊角色，
> 不需要開電腦，也不需要重新貼上任何背景資料。

---

## 前置準備

確認手機已安裝：**Claude by Anthropic**
- iOS：App Store 搜尋「Claude」
- Android：Google Play 搜尋「Claude」

登入與電腦相同的 Anthropic 帳號（rumadragonboat@gmail.com 或你的個人帳號）。

---

## Step 1：在 Claude.ai 建立新 Project

1. 開啟瀏覽器前往 **https://claude.ai**（電腦或手機皆可）
2. 左側側欄點選 **「Projects」**
3. 點選右上角 **「+ New project」** 或 **「建立新專案」**
4. 輸入專案名稱：

   ```
   RUMA Dragon Boat — Virtual AI Team
   ```

5. 點選 **「Create project」**

---

## Step 2：上傳 7 個 SKILL.md 作為 Project Knowledge

進入剛建立的 Project 後，找到 **「Project knowledge」** 或 **「Add content」** 區塊。

依序上傳以下 7 個文件（直接拖曳或點選上傳）：

| 上傳順序 | 檔案路徑 | 說明 |
|---------|---------|------|
| 1 | `CLAUDE.md` | 團隊總覽 + 角色速查 + 常用指令 |
| 2 | `TEAM.md` | 組織架構 + 工具權限表 |
| 3 | `02-Content/WORKFLOW.md` | 自動化流程圖 |
| 4 | `02-Content/ruma-head/SKILL.md` | 主管角色定義 |
| 5 | `02-Content/ruma-head-of-training/SKILL.md` | 訓練長角色定義 |
| 6 | `02-Content/ruma-creative-master/SKILL.md` | 設計師角色定義 |
| 7 | `02-Content/ruma-content-alchemist/SKILL.md` | 內容寫手角色定義 |
| 8 | `02-Content/ruma-seo-master/SKILL.md` | SEO 專家角色定義 |

> 💡 **提示**：不需要上傳 `.env`（API Keys 不要放進 Project Knowledge，安全考量）

---

## Step 3：設定 Project System Prompt

在 Project 設定頁面找到 **「Custom instructions」** 或 **「Project instructions」**，
貼入以下內容：

---

```
你是 RUMA 龍舟隊的虛擬 AI 團隊系統。

## 你的身份
RUMA 是 2024 年成立的台灣多國籍龍舟隊（台灣、馬來西亞、菲律賓、印尼、巴西、阿根廷、美國），
訓練場地在台灣新北市新店區碧潭，官網是 rumadragonboat.com。

## 你管理的 5 個 AI 角色
每個角色的完整工作流程請參考 Project Knowledge 中對應的 SKILL.md。

1. **RUMA_Head**（主管）：審核所有成員交付物，通過後提交 Eric 決策
2. **RUMA_Head_of_Training**（訓練長）：規劃龍舟/重訓/心肺三大訓練課表
3. **RUMA_Visual_Design_Master**（設計師）：產圖、上傳 imgBB、嵌入文章、發布官網
4. **RUMA_Content_Alchemist**（內容寫手）：研究資料、撰寫繁中+英文雙語文章
5. **RUMA_SEO_Master**（SEO 專家）：關鍵字研究、競品分析、文章框架產出

## 對話規則
- Eric 是最終決策者，所有任務由他發起
- 每次對話開始時，如果 Eric 沒有指定角色，主動問他：「請問要啟動哪個角色？」
- 執行任務前，先確認啟動角色，再按照對應 SKILL.md 的工作流程執行
- 如果任務跨越多個角色（如完整內容行銷流程），按照 WORKFLOW.md 的流程依序執行

## 常用啟動方式
- 「SEO」→ 啟動 RUMA_SEO_Master
- 「寫文章」→ 啟動 RUMA_Content_Alchemist
- 「產圖」→ 啟動 RUMA_Visual_Design_Master
- 「訓練」→ 啟動 RUMA_Head_of_Training
- 「審核」→ 啟動 RUMA_Head
- 「全流程」→ 按 WORKFLOW.md 流程 A 完整執行
```

---

貼入後點選 **「Save」** 儲存。

---

## Step 4：在手機 APP 驗證是否成功

1. 開啟手機 **Claude APP**
2. 點選左上角選單（漢堡圖示）
3. 找到 **「Projects」** → 點選 **「RUMA Dragon Boat — Virtual AI Team」**
4. 開始新對話，輸入：

   ```
   請以 RUMA_SEO_Master 的身份，告訴我你的工作職責是什麼
   ```

5. Claude 應該會正確回覆訓練長的詳細角色定義 ✅

---

## Step 5：手機日常使用方式

### 場景一：臨時想到要跑內容行銷

```
全流程跑一次，主題：「龍舟體驗台北新手入門」
```

### 場景二：距比賽還有 6 週，需要訓練計劃

```
請以 RUMA_Head_of_Training 身份，
端午節比賽還有 6 週，規劃完整備賽課表
```

### 場景三：臨時審核一篇文章

直接貼上文章內容，說：

```
請以 RUMA_Head 身份審核以下文章：
[貼上文章內容]
```

### 場景四：臨時跑 SEO 研究

```
以 RUMA_SEO_Master 身份，針對「龍舟重量訓練」做關鍵字研究
```

---

## 方法一 vs 方法二 比較

| 功能 | 方法一（CLAUDE.md）| 方法二（Claude.ai Project）|
|------|-------------------|--------------------------|
| **使用場景** | 電腦 Claude Code CLI | 手機 APP + 電腦網頁 |
| **自動載入** | ✅ 每次 Claude Code 啟動自動載入 | ✅ 進入 Project 後自動套用 |
| **執行工具** | ✅ 可呼叫本地工具（Bash、Read、Write）| ❌ 無法操作本地檔案 |
| **適合任務** | 產圖、發布文章、本地檔案操作 | 腦力任務：寫文章草稿、訓練計劃、SEO 分析 |
| **同步更新** | 需手動更新 `.md` 檔 | 需手動重新上傳文件 |

**建議使用方式：**
- 📱 **手機**：Claude.ai Project → 發想、草稿、計劃
- 💻 **電腦**：Claude Code + CLAUDE.md → 執行、產圖、發布
