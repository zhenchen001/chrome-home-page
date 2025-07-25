# 📚 书签管理完整指南

## 🔍 **当前限制说明**

### **本地开发**
- ✅ 可以读取 Chrome AppData 书签
- ✅ 可以读取 JSON 文件
- ✅ 支持实时同步

### **GitHub Pages 部署**
- ❌ **无法直接读取 Chrome AppData**（浏览器安全限制）
- ✅ 可以读取 JSON 文件
- ✅ 支持网页编辑器

## 🛠️ **解决方案**

### **方案1：导出工具（推荐）**

#### 使用导出工具
1. **关闭 Chrome 浏览器**
2. **运行导出工具**：
   - 双击 `export_bookmarks.bat`
   - 或运行 `python export_bookmarks.py`
3. **上传到 GitHub**：
   - 将生成的 `bookmarks.json` 上传到仓库
   - 提交更改

#### 导出工具特点
- 📋 自动提取所有 Chrome 书签
- 📁 保留文件夹信息（可选）
- 🔍 显示导出预览
- ⚠️ 安全检查和错误处理

### **方案2：手动编辑**

#### 编辑 bookmarks.json
```json
[
  { "name": "GitHub", "url": "https://github.com/" },
  { "name": "你的网站", "url": "https://example.com/" }
]
```

#### 使用网页编辑器
1. 打开网站
2. 点击右上角 ⚙️ 按钮
3. 添加/编辑/删除书签
4. 点击"保存"

**注意**：网页编辑器只保存在浏览器本地存储中

### **方案3：定期同步**

#### 工作流程
1. **本地开发**：使用 Python 服务器读取实时书签
2. **需要部署时**：运行导出工具
3. **上传 JSON**：更新 GitHub Pages

## 📋 **使用建议**

### **初次设置**
1. 使用导出工具获取当前所有书签
2. 上传到 GitHub Pages
3. 根据需要使用网页编辑器微调

### **日常使用**
- **本地开发**：直接使用，实时同步
- **GitHub Pages**：需要时重新导出上传

### **最佳实践**
1. 将常用书签添加到 JSON 文件
2. 使用网页编辑器添加临时书签
3. 定期运行导出工具同步

## 🔄 **同步策略**

网站会按以下优先级加载书签：

1. **本地存储**（网页编辑器保存的）
2. **本地服务器**（开发环境的 Chrome 书签）
3. **JSON 文件**（GitHub Pages 的书签）
4. **默认书签**（备用）

## 📁 **文件说明**

### **新增文件**
- `export_bookmarks.py`：书签导出脚本
- `export_bookmarks.bat`：快速导出工具
- `BOOKMARK_SYNC_GUIDE.md`：本文档

### **现有文件**
- `bookmarks.json`：GitHub Pages 书签数据
- `index.html`：主网页文件
- `bookmarks.py`：本地开发服务器

## 🚀 **部署流程**

### **GitHub Pages 完整流程**
1. **导出书签**：
   ```bash
   python export_bookmarks.py
   ```

2. **上传文件**：
   - `index.html`
   - `bookmarks.json`

3. **启用 Pages**：
   - 仓库设置 → Pages → 选择分支

4. **访问网站**：
   - `https://用户名.github.io/仓库名`

### **更新书签**
1. 运行导出工具
2. 上传新的 `bookmarks.json`
3. 等待 GitHub Pages 更新（通常几分钟）

## ❓ **常见问题**

### **Q: 为什么 GitHub Pages 不能读取 Chrome 书签？**
A: 浏览器安全策略禁止网页访问本地文件系统。

### **Q: 网页编辑器的书签会丢失吗？**
A: 存储在浏览器本地存储中，清除浏览器数据时会丢失。

### **Q: 如何保持书签同步？**
A: 重要书签放在 JSON 文件中，临时书签使用网页编辑器。

### **Q: 导出工具无法运行？**
A: 确保 Chrome 完全关闭，检查文件权限。
