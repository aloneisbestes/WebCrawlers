# 需求: 爬取搜狗首页的页面数据。

# 导入 requests 模块
import requests

if __name__ == "__main__":
    # 1. 指定 url
    url = "https://www.sogou.com/"
    # 2. 发送请求
    response = requests.get(url=url)
    # 3. 获取响应数据
    ret_str = response.text # 字符串形式的响应数据
    print(ret_str)
    # 4. 持久化存储
    with open('./sogou.html', 'w', encoding='utf-8') as fp:
        fp.write(ret_str)
    print("爬取数据结束。")