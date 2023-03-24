import requests
from bs4 import BeautifulSoup

# 设置请求头部
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
}

# 搜索关键词
query = '青蛙'

# 构造搜索引擎链接
url = f'https://www.baidu.com/s?wd={query}'

# 发送HTTP请求并获取响应内容
response = requests.get(url, headers=headers)
html = response.text

# 使用BeautifulSoup解析HTML
soup = BeautifulSoup(html, 'html.parser')

# 获取搜索结果的列表
result_list = soup.find_all('div', class_='result c-container xpath-log new-pmd')

# 遍历每个搜索结果并提取标题和链接
for result in result_list:
    # 提取标题
    title = result.h3.text.strip()

    # 提取链接
    link = result.a['href']

    # 打印标题和链接
    print(f'{title}: {link}\n')
