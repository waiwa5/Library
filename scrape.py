import requests
import sys

url = "https://sites.google.com/view/waylonlee/home"

# 增加更真实的浏览器伪装头
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.5"
}

try:
    print(f"正在抓取网页: {url}")
    response = requests.get(url, headers=headers, timeout=10)
    
    # 如果遇到 404, 403 等错误，直接抛出异常
    response.raise_for_status() 
    
    output_filename = "google_site_content.html"
    with open(output_filename, "w", encoding="utf-8") as f:
        f.write(response.text)
        
    print(f"✅ 成功！网页内容已保存到 {output_filename}")

except requests.exceptions.RequestException as e:
    # 遇到错误时，打印错误并强制程序以失败状态(exit code 1)退出
    print(f"❌ 抓取失败: {e}")
    sys.exit(1)
