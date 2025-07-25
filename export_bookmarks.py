import json
import os
import sys

def export_chrome_bookmarks():
    """
    从 Chrome 导出书签到 bookmarks.json 文件
    用于 GitHub Pages 部署
    """
    try:
        # 書籤檔案路徑
        user = os.getlogin()
        bookmark_path = f"C:/Users/{user}/AppData/Local/Google/Chrome/User Data/Default/Bookmarks"
        
        print(f"正在读取 Chrome 书签: {bookmark_path}")
        
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
                # 如果需要，可以添加文件夹信息
                if folder_name and folder_name not in ["書籤列", "其他書籤", "行動書籤"]:
                    bookmark["folder"] = folder_name
                bookmarks.append(bookmark)
        
        # 開始提取所有書籤
        roots = data.get("roots", {})
        for root_name, root in roots.items():
            if root_name in ["bookmark_bar", "other", "synced"]:  # 只导出主要书签
                extract_bookmarks(root)
        
        # 保存到 JSON 文件
        output_file = "bookmarks.json"
        with open(output_file, "w", encoding="utf-8") as f:
            json.dump(bookmarks, f, ensure_ascii=False, indent=2)
        
        print(f"✅ 成功导出 {len(bookmarks)} 个书签到 {output_file}")
        print(f"📁 文件位置: {os.path.abspath(output_file)}")
        print("\n📋 导出的书签预览:")
        for i, bookmark in enumerate(bookmarks[:10]):  # 显示前10个
            folder_info = f" [{bookmark.get('folder', '')}]" if bookmark.get('folder') else ""
            print(f"  {i+1}. {bookmark['name']}{folder_info}")
            print(f"     {bookmark['url']}")
        
        if len(bookmarks) > 10:
            print(f"  ... 还有 {len(bookmarks) - 10} 个书签")
        
        print(f"\n🚀 现在您可以将 {output_file} 上传到 GitHub Pages!")
        
        return bookmarks
        
    except FileNotFoundError:
        print("❌ 错误: 找不到 Chrome 书签文件")
        print("请确保:")
        print("1. Chrome 浏览器已安装")
        print("2. Chrome 浏览器已完全关闭")
        print("3. 至少使用过一次 Chrome 浏览器")
        return None
        
    except PermissionError:
        print("❌ 错误: 权限不足，无法读取书签文件")
        print("请确保 Chrome 浏览器已完全关闭")
        return None
        
    except Exception as e:
        print(f"❌ 错误: {e}")
        return None

def main():
    print("🔖 Chrome 书签导出工具")
    print("=" * 40)
    print("此工具将 Chrome 书签导出为 bookmarks.json 文件")
    print("用于 GitHub Pages 部署\n")
    
    # 检查是否存在现有文件
    if os.path.exists("bookmarks.json"):
        print("⚠️  发现现有的 bookmarks.json 文件")
        choice = input("是否覆盖? (y/N): ").lower().strip()
        if choice not in ['y', 'yes', '是']:
            print("操作已取消")
            return
    
    print("正在导出书签...")
    bookmarks = export_chrome_bookmarks()
    
    if bookmarks:
        print("\n✨ 导出完成!")
        print("\n📝 下一步:")
        print("1. 将 bookmarks.json 上传到您的 GitHub 仓库")
        print("2. 提交更改到 GitHub")
        print("3. GitHub Pages 会自动更新")
        print("4. 访问您的网站查看新书签")
    else:
        print("\n💡 提示:")
        print("如果继续遇到问题，您也可以:")
        print("1. 手动编辑 bookmarks.json 文件")
        print("2. 使用网页上的编辑器添加书签")
    
    input("\n按 Enter 键退出...")

if __name__ == "__main__":
    main()
