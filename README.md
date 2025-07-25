# Chrome 書籤首頁

這個項目會讀取你的 Chrome 瀏覽器書籤，並在一個美觀的首頁中顯示它們。支持本地開發和 GitHub Pages 部署。

## ⚠️ **重要說明：書籤讀取限制**

### **本地開發環境**
- ✅ **可以直接讀取** Chrome AppData 中的書籤文件
- ✅ 實時同步，無需手動更新
- ✅ 完整功能支持

### **GitHub Pages 部署**
- ❌ **無法直接讀取** Chrome AppData（瀏覽器安全限制）
- ✅ 只能讀取 `bookmarks.json` 文件
- ✅ 支持網頁編輯器自定義書籤

## 🛠️ **GitHub Pages 解決方案**

### **方案1：使用導出工具（推薦）**
1. 雙擊 `export_bookmarks.bat` 或運行 `python export_bookmarks.py`
2. 將生成的 `bookmarks.json` 上傳到 GitHub
3. 書籤會在網站上顯示

### **方案2：手動編輯**
直接編輯 `bookmarks.json` 文件添加您的書籤

### **方案3：網頁編輯器**
使用網站右上角的 ⚙️ 按鈕編輯書籤（存儲在瀏覽器本地）

詳細說明請查看：**[書籤同步完整指南](BOOKMARK_SYNC_GUIDE.md)**

## 🌐 GitHub Pages 部署（推薦）

如果您想在 GitHub Pages 上部署，請查看 **[GitHub Pages 部署指南](GITHUB_PAGES_GUIDE.md)**

### 快速部署
1. 將 `index.html` 和 `bookmarks.json` 上傳到 GitHub 倉庫
2. 在倉庫設置中啟用 GitHub Pages
3. 編輯 `bookmarks.json` 來自定義您的書籤
4. 訪問 `https://您的用戶名.github.io/倉庫名稱`

## 💻 本地開發使用方法

### 方法一：使用批處理文件（推薦）
1. 雙擊 `start_server.bat` 文件
2. 等待服務器啟動（會顯示"書籤服務器啟動在 http://localhost:8000"）
3. 在瀏覽器中打開 `index.html` 文件

### 方法二：手動啟動
1. 打開命令提示符或 PowerShell
2. 切換到此資料夾：`cd "c:\Users\USER\Documents\Py\新增資料夾"`
3. 運行：`python bookmarks.py`
4. 在瀏覽器中打開 `index.html` 文件

## ✨ 功能特點

### 📚 多重書籤來源
- **本地存儲**：網頁內編輯的自定義書籤
- **Chrome 書籤**：本地開發時自動讀取
- **JSON 文件**：GitHub Pages 部署時的書籤來源
- **默認書籤**：備用書籤列表

### ⚙️ 書籤編輯
- 點擊右上角 ⚙️ 按鈕開啟編輯器
- 添加、修改、刪除書籤
- 自動保存到瀏覽器本地存儲

### 📱 響應式設計
- 適配桌面和移動設備
- 美觀的深色主題
- 流暢的動畫效果

## 📁 文件說明

- `index.html`：主要網頁文件，包含所有功能
- `bookmarks.py`：Python 服務器，用於本地開發
- `bookmarks.json`：書籤數據文件，用於 GitHub Pages
- `start_server.bat`：快速啟動服務器的批處理文件
- `GITHUB_PAGES_GUIDE.md`：詳細的 GitHub Pages 部署指南

## ⚠️ 注意事項

### 本地開發
- **重要**：在啟動服務器之前，請確保 Chrome 瀏覽器已完全關閉
- 如果無法讀取 Chrome 書籤，頁面會顯示默認的書籤列表
- 服務器會在 http://localhost:8000 運行
- 按 Ctrl+C 可以停止服務器

### GitHub Pages 部署
- 無法讀取本地 Chrome 書籤（安全限制）
- 書籤數據來自 `bookmarks.json` 文件
- 網頁編輯器的更改只保存在瀏覽器本地存儲中

## 🔧 故障排除

### 書籤沒有正確顯示
1. **本地開發**：確認 Chrome 瀏覽器已完全關閉
2. **GitHub Pages**：檢查 `bookmarks.json` 文件格式
3. 檢查瀏覽器開發者工具中的控制台錯誤信息
4. 確認相關文件路徑是否正確

### 無法連接到服務器
1. 確認 Python 服務器正在運行
2. 檢查防火牆設置
3. 嘗試使用 `http://127.0.0.1:8000/bookmarks` 直接訪問 API

### GitHub Pages 無法訪問
1. 確認 GitHub Pages 已正確啟用
2. 等待幾分鐘讓更改生效
3. 檢查倉庫是否為公開狀態
