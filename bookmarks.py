import json
import os
from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import urlparse, parse_qs
import threading

class BookmarkHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        parsed_path = urlparse(self.path)
        
        # 添加 CORS 头
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.end_headers()
        
        if parsed_path.path == '/bookmarks':
            bookmarks = get_chrome_bookmarks()
            self.wfile.write(json.dumps(bookmarks, ensure_ascii=False).encode('utf-8'))
        else:
            self.wfile.write(json.dumps({"error": "Endpoint not found"}).encode('utf-8'))
    
    def do_OPTIONS(self):
        # 处理预检请求
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.end_headers()

def get_chrome_bookmarks():
    try:
        # 書籤檔案路徑
        user = os.getlogin()
        bookmark_path = f"C:/Users/{user}/AppData/Local/Google/Chrome/User Data/Default/Bookmarks"
        
        with open(bookmark_path, "r", encoding="utf-8") as f:
            data = json.load(f)
        
        bookmarks = []
        
        def extract_bookmarks(bookmark_node):
            if "children" in bookmark_node:
                for node in bookmark_node["children"]:
                    extract_bookmarks(node)
            elif bookmark_node.get("type") == "url":
                bookmarks.append({
                    "name": bookmark_node.get("name", ""),
                    "url": bookmark_node.get("url", "")
                })
        
        # 開始提取所有書籤
        roots = data.get("roots", {})
        for root in roots.values():
            extract_bookmarks(root)
            
        return bookmarks
        
    except Exception as e:
        print(f"Error reading bookmarks: {e}")
        return [
            {"name": "GitHub", "url": "https://github.com/"},
            {"name": "Google 翻譯", "url": "https://translate.google.com/"},
            {"name": "YouTube", "url": "https://youtube.com/"},
            {"name": "維基百科", "url": "https://zh.wikipedia.org/"}
        ]

def start_server():
    server_address = ('', 8000)
    httpd = HTTPServer(server_address, BookmarkHandler)
    print("書籤服務器啟動在 http://localhost:8000")
    print("請在瀏覽器中打開 index.html")
    print("按 Ctrl+C 停止服務器")
    httpd.serve_forever()

if __name__ == "__main__":
    start_server()