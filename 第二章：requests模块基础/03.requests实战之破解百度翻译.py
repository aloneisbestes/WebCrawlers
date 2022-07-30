# 导入 requests 模块
import requests
import json

if __name__ == "__main__":
    # User-Agent 伪装
    headers = {
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"
    }

    # 指定 url
    post_url = "https://fanyi.baidu.com/sug"

    # url 携带的参数
    word = input("enter a word: ")
    data = {
        'kw' : word
    }

    # 发送请求
    """
    data: 请求参数
    headers: 请求头封装
    url: 请求路径
    """
    response = requests.post(url=post_url, data=data, headers=headers)

    # 获取数据, json 方法返回的是一个 object
    ret_json = response.json()
    print(ret_json)

    # 保存数据
    ffileName = word+".json"
    fp = open(ffileName, 'w', encoding='utf-8')
    # ensure_ascii = false 表示不使用 ascii
    json.dump(ret_json, fp=fp, ensure_ascii=False)
    print("over!!")