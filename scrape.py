import requests
import os

# 你的 Google Site 链接
url = "https://sites.google.com/view/waylonlee/home"

# 设置请求头，伪装成浏览器，防止被直接拦截
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"
}

try:
    print(f"正在抓取网页: {url}")
    response = requests.get(url, headers=headers)
    response.raise_for_status() # 检查请求是否成功
    
    # 将抓取到的 HTML 保存到本地文件中
    # 我们把它保存在仓库的一个特定目录里，比如直接放在根目录
    output_filename = "google_site_content.html"
    
    with open(output_filename, "w", encoding="utf-8") as f:
        f.write(response.text)
        
    print(f"成功！网页内容已保存到 {output_filename}")

except Exception as e:
    print(f"抓取失败: {e}")