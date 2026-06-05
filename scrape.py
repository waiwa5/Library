from playwright.sync_api import sync_playwright
import sys

url = "https://sites.google.com/view/waylonlee/home"

with sync_playwright() as p:
    # 启动一个隐藏的 Chromium 浏览器
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()
    try:
        print(f"正在模拟真实浏览器打开网页: {url}")
        # wait_until="networkidle" 表示等待页面上的动态内容和网络请求都加载完毕
        page.goto(url, timeout=30000, wait_until="networkidle")
        
        # 获取渲染后的完整 HTML
        content = page.content()
        
        with open("google_site_content.html", "w", encoding="utf-8") as f:
            f.write(content)
            
        print("✅ 成功！页面已保存。")
    except Exception as e:
        print(f"❌ 抓取失败: {e}")
        sys.exit(1)
    finally:
        browser.close()