from playwright.sync_api import sync_playwright
import sys

url = "https://sites.google.com/view/waylonlee/home"

try:
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        
        # --- 新增：顶级伪装术 ---
        # 伪装成一台 1080P 屏幕的 Windows 电脑，使用最新版 Chrome
        context = browser.new_context(
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
            viewport={'width': 1920, 'height': 1080}
        )
        page = context.new_page()
        # ------------------------

        print(f"正在模拟真实浏览器打开网页: {url}")
        
        # 增加等待时间，确保动态内容加载完毕
        page.goto(url, timeout=60000, wait_until="networkidle")
        
        # 获取完整的 HTML
        content = page.content()
        
        with open("google_site_content.html", "w", encoding="utf-8") as f:
            f.write(content)
            
        print("✅ 成功！带有伪装的页面内容已保存。")
        browser.close()
except Exception as e:
    print(f"❌ 抓取失败: {e}")
    sys.exit(1)
