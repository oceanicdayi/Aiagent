# Hugging Face Spaces 部署指南

本指南詳細說明如何將此項目部署到 Hugging Face Spaces。

## 前置準備

1. **Hugging Face 帳號**: 註冊 [Hugging Face](https://huggingface.co/join)
2. **GitHub 倉庫 URL**: 確保您有要安裝的套件的正確 GitHub URL

## 部署步驟

### 方法 1: 通過 Web 界面

1. **訪問 Hugging Face Spaces**
   - 前往 https://huggingface.co/spaces
   - 點擊右上角的 "New Space" 按鈕

2. **配置 Space**
   - **Owner**: 選擇您的用戶名或組織
   - **Space name**: 輸入名稱（例如：openclaw-demo）
   - **License**: 選擇許可證（建議：apache-2.0 或 mit）
   - **SDK**: 選擇 "Gradio"
   - **Space hardware**: 選擇 "CPU basic"（免費）或根據需要選擇其他選項
   - **Visibility**: 選擇 Public 或 Private

3. **上傳文件**
   - 點擊 "Files" 標籤
   - 上傳以下文件：
     - `app.py`
     - `requirements.txt`
     - `README.md`（可選）
   - 或使用 Git 推送（見方法 2）

4. **等待構建**
   - Hugging Face 會自動開始構建
   - 在 "Logs" 標籤中查看構建進度
   - 構建成功後，應用會自動啟動

### 方法 2: 通過 Git 推送

1. **克隆 Space 倉庫**
   ```bash
   git clone https://huggingface.co/spaces/YOUR_USERNAME/YOUR_SPACE_NAME
   cd YOUR_SPACE_NAME
   ```

2. **配置 Git LFS**（如需處理大文件）
   ```bash
   git lfs install
   ```

3. **複製項目文件**
   ```bash
   cp /path/to/Aiagent/app.py .
   cp /path/to/Aiagent/requirements.txt .
   cp /path/to/Aiagent/README.md .
   ```

4. **提交並推送**
   ```bash
   git add .
   git commit -m "Initial deployment"
   git push
   ```

5. **查看部署**
   - 訪問 https://huggingface.co/spaces/YOUR_USERNAME/YOUR_SPACE_NAME
   - 檢查構建日誌和運行狀態

## 配置 requirements.txt

### 選項 1: 使用 tarball URL
```txt
https://github.com/TigerResearch/OpenCLAW/archive/refs/heads/master.tar.gz
gradio>=3.50.0
```

### 選項 2: 使用 Git 協議（推薦）
```txt
git+https://github.com/TigerResearch/OpenCLAW.git@master
gradio>=3.50.0
```

### 選項 3: 指定特定版本
```txt
git+https://github.com/TigerResearch/OpenCLAW.git@v1.0.0
gradio>=3.50.0
```

### 選項 4: 私有倉庫
如果是私有倉庫，需要在 Space 設置中添加 Secrets：

1. 在 Space 頁面，點擊 "Settings"
2. 在 "Repository secrets" 部分添加 `GITHUB_TOKEN`
3. 在 requirements.txt 中使用：
```txt
git+https://${GITHUB_TOKEN}@github.com/TigerResearch/OpenCLAW.git@master
gradio>=3.50.0
```

## 驗證部署

部署成功後：

1. **檢查 Space 狀態**: Space 應該顯示為 "Running"
2. **訪問應用**: 點擊 Space URL 查看應用界面
3. **查看日誌**: 
   - 在 "Logs" 標籤查看運行時日誌
   - 確認沒有錯誤訊息
4. **測試功能**: 
   - 測試 "Demo" 標籤的問候功能
   - 檢查 "System Info" 標籤確認套件安裝狀態

## 故障排除

### 構建失敗

**症狀**: Space 顯示 "Build error" 或卡在構建階段

**解決方案**:
1. 檢查 "Logs" 標籤查看詳細錯誤
2. 常見問題：
   - **依賴衝突**: 調整 requirements.txt 中的版本號
   - **套件不存在**: 驗證 GitHub URL 是否正確
   - **私有倉庫**: 確保已配置 GITHUB_TOKEN

### 運行時錯誤

**症狀**: 構建成功但應用無法啟動

**解決方案**:
1. 檢查運行時日誌
2. 常見問題：
   - **Import 錯誤**: 套件名稱可能與倉庫名稱不同
   - **缺少依賴**: 在 requirements.txt 中添加遺漏的依賴
   - **端口問題**: Gradio 應用應該使用 `demo.launch()` 不指定端口

### Space 超時

**症狀**: Space 顯示 "Sleeping" 或超時

**解決方案**:
1. 免費 Space 在閒置後會休眠
2. 訪問 Space URL 會自動喚醒
3. 考慮升級到付費計劃以保持持續運行

## 更新部署

### 通過 Web 界面
1. 訪問 Space 頁面
2. 點擊 "Files" 標籤
3. 選擇要更新的文件
4. 點擊 "Edit" 進行編輯
5. 保存後自動重新構建

### 通過 Git
```bash
cd YOUR_SPACE_NAME
# 修改文件
git add .
git commit -m "Update description"
git push
```

## 最佳實踐

1. **版本固定**: 在 requirements.txt 中使用特定版本號
   ```txt
   gradio==3.50.2  # 而不是 gradio>=3.50.0
   ```

2. **測試本地**: 在推送到 Hugging Face 之前本地測試
   ```bash
   python -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   python app.py
   ```

3. **監控日誌**: 定期檢查運行日誌以發現潛在問題

4. **文檔完整**: 在 README.md 中包含使用說明

5. **優雅降級**: 如果可選套件安裝失敗，應用應該能夠降級運行

## 相關資源

- [Hugging Face Spaces 文檔](https://huggingface.co/docs/hub/spaces)
- [Gradio 文檔](https://gradio.app/docs/)
- [Python pip 安裝指南](https://pip.pypa.io/en/stable/cli/pip_install/)
- [Git 基礎教程](https://git-scm.com/book/zh/v2)

## 支持

如果遇到問題：
1. 查看 [Hugging Face 論壇](https://discuss.huggingface.co/)
2. 查看本倉庫的 Issues
3. 查看 Gradio 社區資源
