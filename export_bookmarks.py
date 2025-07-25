import json
import os
import sys

def export_chrome_bookmarks():
    """
    從 Chrome 導出書籤到 bookmarks.json 文件
    用於 GitHub Pages 部署
    """
    try:
        # 書籤檔案路徑
        user = os.getlogin()
        bookmark_path = f"C:/Users/{user}/AppData/Local/Google/Chrome/User Data/Default/Bookmarks"
        
        print(f"正在讀取 Chrome 書籤: {bookmark_path}")
        
        with open(bookmark_path, "r", encoding="utf-8") as f:
            data = json.load(f)
        
        bookmarks = []
        
        def extract_bookmarks(bookmark_node, folder_name=""):
            if "children" in bookmark_node:
                current_folder = bookmark_node.get("name", folder_name)
                for node in bookmark_node["children"]:
                    extract_bookmarks(node, current_folder)
            elif bookmark_node.get("type") == "url":
                bookmark = {
                    "name": bookmark_node.get("name", ""),
                    "url": bookmark_node.get("url", "")
                }
                # 如果需要，可以添加資料夾信息
                if folder_name and folder_name not in ["書籤列", "其他書籤", "行動書籤"]:
                    bookmark["folder"] = folder_name
                bookmarks.append(bookmark)
        
        # 開始提取所有書籤
        roots = data.get("roots", {})
        for root_name, root in roots.items():
            if root_name in ["bookmark_bar", "other", "synced"]:  # 只導出主要書籤
                extract_bookmarks(root)
        
        # 保存到 JSON 文件
        output_file = "bookmarks.json"
        with open(output_file, "w", encoding="utf-8") as f:
            json.dump(bookmarks, f, ensure_ascii=False, indent=2)
        
        print(f"✅ 成功導出 {len(bookmarks)} 個書籤到 {output_file}")
        print(f"📁 文件位置: {os.path.abspath(output_file)}")
        print("\n📋 導出的書籤預覽:")
        for i, bookmark in enumerate(bookmarks[:10]):  # 顯示前10個
            folder_info = f" [{bookmark.get('folder', '')}]" if bookmark.get('folder') else ""
            print(f"  {i+1}. {bookmark['name']}{folder_info}")
            print(f"     {bookmark['url']}")
        
        if len(bookmarks) > 10:
            print(f"  ... 還有 {len(bookmarks) - 10} 個書籤")
        
        print(f"\n🚀 現在您可以將 {output_file} 上傳到 GitHub Pages!")
        
        return bookmarks
        
    except FileNotFoundError:
        print("❌ 錯誤: 找不到 Chrome 書籤文件")
        print("請確保:")
        print("1. Chrome 瀏覽器已安裝")
        print("2. Chrome 瀏覽器已完全關閉")
        print("3. 至少使用過一次 Chrome 瀏覽器")
        return None
        
    except PermissionError:
        print("❌ 錯誤: 權限不足，無法讀取書籤文件")
        print("請確保 Chrome 瀏覽器已完全關閉")
        return None
        
    except Exception as e:
        print(f"❌ 錯誤: {e}")
        return None

def main():
    print("🔖 Chrome 書籤導出工具")
    print("=" * 40)
    print("此工具將 Chrome 書籤導出為 bookmarks.json 文件")
    print("用於 GitHub Pages 部署\n")
    
    # 檢查是否存在現有文件
    if os.path.exists("bookmarks.json"):
        print("⚠️  發現現有的 bookmarks.json 文件")
        choice = input("是否覆蓋? (y/N): ").lower().strip()
        if choice not in ['y', 'yes', '是']:
            print("操作已取消")
            return
    
    print("正在導出書籤...")
    bookmarks = export_chrome_bookmarks()
    
    if bookmarks:
        print("\n✨ 導出完成!")
        print("\n📝 下一步:")
        print("1. 將 bookmarks.json 上傳到您的 GitHub 倉庫")
        print("2. 提交更改到 GitHub")
        print("3. GitHub Pages 會自動更新")
        print("4. 訪問您的網站查看新書籤")
    else:
        print("\n💡 提示:")
        print("如果繼續遇到問題，您也可以:")
        print("1. 手動編輯 bookmarks.json 文件")
        print("2. 使用網頁上的編輯器添加書籤")
    
    input("\n按 Enter 鍵退出...")

if __name__ == "__main__":
    main()
