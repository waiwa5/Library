name: Auto Scrape Google Site

on:
  schedule:
    - cron: '0 0 * * *'
  workflow_dispatch: 

# 新增这行环境变量，强制使用最新的 Node.js 24，彻底消除警告
env:
  FORCE_JAVASCRIPT_ACTIONS_TO_NODE24: true 

jobs:
  scrape-and-commit:
    runs-on: ubuntu-latest

    steps:
    - name: 检出代码仓库
      # 升级到 v4
      uses: actions/checkout@v4 

    - name: 配置 Python 环境
      # 升级到 v5
      uses: actions/setup-python@v5 
      with:
        python-version: '3.10'

    - name: 安装依赖
      run: |
        pip install -r requirements.txt

    - name: 运行抓取脚本
      run: |
        python scrape.py

    - name: 检查文件是否有变动并提交
      run: |
        git config --local user.email "action@github.com"
        git config --local user.name "GitHub Action Bot"
        git add google_site_content.html
        
        if ! git diff-index --quiet HEAD; then
          git commit -m "Auto-update: 同步最新的 Google Site 内容"
          git push
        else
          echo "内容没有变化，无需提交。"
        fi
