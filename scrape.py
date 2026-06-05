from playwright.sync_api import sync_playwright
import sys

url = "https://sites.google.com/view/waylonlee/home"

try:
    with sync_playwright() as p:
        # 启动虚拟 Chrome
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        print(f"正在模拟真实浏览器打开网页: {url}")
        
        # wait_until="networkidle" 确保 Google Site 的动态 JS 内容完全加载
        page.goto(url, timeout=60000, wait_until="networkidle")
        
        # 提取渲染后的 HTML
        content = page.content()
        
        with open("google_site_content.html", "w", encoding="utf-8") as f:
            f.write(content)
            
        print("✅ 成功！页面内容已保存。")
        browser.close()
except Exception as e:
    print(f"❌ 抓取失败: {e}")
    sys.exit(1)
