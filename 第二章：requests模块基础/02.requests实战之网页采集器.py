# 导入 requests 模块
import requests

if __name__ == "__main__":
    # User-Agent 伪装
    headers = {
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"
    }

    # 处理 url 携带的参数
    url = "https://www.sogou.com/web"
    # 把存储封装到字典中
    kw = input('enter a word: ')
    param = {
        'query': kw
    }

    # 发送请求，对指定的 url 发送请求是携带参数，并且请求过程中处理了参数
    response = requests.get(url=url, params=param, headers=headers)

    # 获取响应数据
    page_text = response.text

    # 保存数据
    fileName = kw+'.html'
    with open(fileName, 'w', encoding='utf-8') as fp:
        fp.write(page_text)

    print(fileName, '保存成功!!')
