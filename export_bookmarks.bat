@echo off
chcp 65001 >nul
echo.
echo ══════════════════════════════════════
echo    Chrome 书签导出工具
echo ══════════════════════════════════════
echo.
echo 此工具将导出您的 Chrome 书签为 JSON 文件
echo 用于 GitHub Pages 部署
echo.
echo ⚠️  请确保 Chrome 浏览器已完全关闭！
echo.
pause
echo.
echo 正在运行导出工具...
echo.
python export_bookmarks.py
echo.
pause
