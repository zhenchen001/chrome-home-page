# Chrome 書籤首頁

這個項目會讀取你的 Chrome 瀏覽器書籤，並在一個美觀的首頁中顯示它們。

## 使用方法

### 方法一：使用批處理文件（推薦）
1. 雙擊 `start_server.bat` 文件
2. 等待服務器啟動（會顯示"書籤服務器啟動在 http://localhost:8000"）
3. 在瀏覽器中打開 `index.html` 文件

### 方法二：手動啟動
1. 打開命令提示符或 PowerShell
2. 切換到此資料夾：`cd "c:\Users\USER\Documents\Py\新增資料夾"`
3. 運行：`python bookmarks.py`
4. 在瀏覽器中打開 `index.html` 文件

## 注意事項

- **重要**：在啟動服務器之前，請確保 Chrome 瀏覽器已完全關閉
- 如果無法讀取 Chrome 書籤，頁面會顯示默認的書籤列表
- 服務器會在 http://localhost:8000 運行
- 按 Ctrl+C 可以停止服務器

## 文件說明

- `bookmarks.py`：Python 服務器，讀取 Chrome 書籤並提供 API
- `index.html`：美觀的首頁界面
- `start_server.bat`：快速啟動服務器的批處理文件

## 故障排除

如果書籤沒有正確顯示：
1. 確認 Chrome 瀏覽器已完全關閉
2. 檢查 Python 服務器是否正在運行
3. 在瀏覽器開發者工具中查看控制台錯誤信息
4. 確認 Chrome 書籤文件路徑是否正確
