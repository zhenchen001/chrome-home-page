@echo off
chcp 65001 >nul
echo.
echo ══════════════════════════════════════
echo    Chrome 書籤導出工具
echo ══════════════════════════════════════
echo.
echo 此工具將導出您的 Chrome 書籤為 JSON 文件
echo 用於 GitHub Pages 部署
echo.
echo ⚠️  請確保 Chrome 瀏覽器已完全關閉！
echo.
pause
echo.
echo 正在運行導出工具...
echo.
python export_bookmarks.py
echo.
pause
