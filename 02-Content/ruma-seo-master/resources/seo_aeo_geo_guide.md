# SEO/AEO/GEO 完整策略指南

本指南整合 SEO（搜尋引擎優化）、AEO（AI 答案引擎優化）、GEO（地域性搜尋優化）三大策略，供 RUMA 龍舟隊文章使用。

> 詳細的使用規範已整合於 `../SKILL.md` 主檔中，本文件作為延伸參考。

---

## 一、SEO 檢查清單

### 發文前必檢
- [ ] 標題含主關鍵字，60 字元內
- [ ] Meta description 150-160 字元，含 CTA
- [ ] URL slug 簡短且含關鍵字
- [ ] H1 唯一，H2-H4 標題結構正確
- [ ] 內部連結至 RUMA 其他頁面（至少 2-3 個）
- [ ] 圖片 alt 文字含關鍵字
- [ ] 首段包含主關鍵字
- [ ] 關鍵字密度 1-2%（自然分佈）

### AEO 優化必檢
- [ ] 直接回答式開場 (Position Zero 優化)
- [ ] FAQ Schema 結構化資料（5-8 個問答）
- [ ] HowTo Schema（適用教學文）
- [ ] 清晰的步驟列表
- [ ] 表格整理比較資訊
- [ ] 定義框解釋專業術語

### GEO 優化必檢
- [ ] 地點名稱自然融入（如：台北大佳河濱公園）
- [ ] 在地化用語（台灣用語，非中國用語）
- [ ] Google My Business 相關連結（若適用）

---

## 二、Schema 範例庫

### Article Schema
```json
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "龍舟新手完整入門指南",
  "author": {
    "@type": "Organization",
    "name": "RUMA 龍舟隊"
  },
  "publisher": {
    "@type": "Organization",
    "name": "RUMA Dragon Boat",
    "url": "https://rumadragonboat.com"
  },
  "datePublished": "2026-02-18",
  "description": "第一次划龍舟不知道怎麼開始？...",
  "image": "https://rumadragonboat.com/images/beginner-guide-cover.jpg"
}
```

### FAQPage Schema
```json
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "第一次划龍舟會很難嗎？",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "龍舟對新手非常友善！基本動作在 30 分鐘內就能學會。"
      }
    },
    {
      "@type": "Question",
      "name": "龍舟體驗需要會游泳嗎？",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "建議具備基本游泳能力，但練習時全程穿著救生衣。"
      }
    }
  ]
}
```

### SportsEvent Schema
```json
{
  "@context": "https://schema.org",
  "@type": "SportsEvent",
  "name": "RUMA 龍舟體驗活動",
  "location": {
    "@type": "Place",
    "name": "大佳河濱公園",
    "address": "台北市中山區"
  },
  "organizer": {
    "@type": "Organization",
    "name": "RUMA Dragon Boat"
  }
}
```

---

## 三、競品分析模板

```markdown
## 競品分析：[關鍵字]

### Google 搜尋前三名

| 排名 | 網站 | 標題 | 字數 | 優點 | 缺點 |
|------|------|------|------|------|------|
| 1 | xxx | xxx | xxx | xxx | xxx |
| 2 | xxx | xxx | xxx | xxx | xxx |
| 3 | xxx | xxx | xxx | xxx | xxx |

### 差異化機會
- [ ] 缺少的主題：
- [ ] 可以更深入的角度：
- [ ] 缺少的 Schema：
- [ ] 我們的獨特優勢（RUMA 一手經驗）：
```

---

## 四、發布後監測

### 監測工具
- **Google Search Console**：關鍵字排名、點擊率、曝光
- **Google Analytics (GA4)**：流量、停留時間、跳出率
- **AI 工具**：定期測試 ChatGPT/Gemini 是否引用我們內容

### 更新策略
- 每 3-6 個月更新長青內容
- 新增最新資訊與案例
- 優化表現不佳的段落
- 追蹤關鍵字排名變化
