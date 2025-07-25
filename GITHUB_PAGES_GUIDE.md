# GitHub Pages 部署指南

## 快速部署步驟

### 1. 創建 GitHub 倉庫
1. 登入 GitHub
2. 創建新倉庫（建議名為 `my-homepage` 或類似名稱）
3. 上傳這些文件：
   - `index.html`
   - `bookmarks.json`
   - `README.md`

### 2. 啟用 GitHub Pages
1. 進入倉庫設置 (Settings)
2. 找到 "Pages" 選項
3. 在 "Source" 下選擇 "Deploy from a branch"
4. 選擇 "main" 分支和 "/ (root)" 文件夾
5. 點擊 "Save"

### 3. 訪問您的網站
- 網址格式：`https://您的用戶名.github.io/倉庫名稱`
- 例如：`https://john.github.io/my-homepage`

## 自定義書籤

### 方法一：編輯 bookmarks.json 文件
直接在 GitHub 上編輯 `bookmarks.json` 文件：
```json
[
  { "name": "GitHub", "url": "https://github.com/" },
  { "name": "您的網站", "url": "https://example.com/" }
]
```

### 方法二：使用網頁編輯器
1. 打開您的網站
2. 點擊右上角的 ⚙️ 按鈕
3. 添加、編輯或刪除書籤
4. 點擊"保存"

**注意**：使用網頁編輯器的更改只會保存在瀏覽器本地存儲中，不會同步到 GitHub。

## 文件說明

### index.html
- 主要的網頁文件
- 包含搜索功能和書籤顯示
- 支持響應式設計

### bookmarks.json
- 書籤數據文件
- JSON 格式，易於編輯
- 網站會自動讀取此文件

## 功能特點

### ✅ GitHub Pages 兼容
- 純前端實現，無需服務器
- 自動從 JSON 文件讀取書籤
- 支持本地存儲自定義書籤

### ✅ 多重書籤來源
1. 本地存儲（用戶自定義）
2. 本地 Python 服務器（開發環境）
3. JSON 文件（GitHub Pages）
4. 默認書籤（備用）

### ✅ 編輯功能
- 網頁內編輯器
- 添加/刪除/修改書籤
- 本地存儲保存

## 故障排除

### 書籤沒有顯示
1. 檢查 `bookmarks.json` 文件格式是否正確
2. 確認 GitHub Pages 已正確啟用
3. 查看瀏覽器開發者工具的控制台錯誤

### 自定義書籤丟失
- 清除瀏覽器數據會刪除本地存儲的自定義書籤
- 建議將重要書籤添加到 `bookmarks.json` 文件中

### 網站無法訪問
- GitHub Pages 啟用後可能需要幾分鐘才能生效
- 檢查倉庫是否為公開狀態
- 確認文件名為 `index.html`（小寫）
