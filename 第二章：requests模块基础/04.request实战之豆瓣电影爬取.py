import requests
import json

if __name__ == "__main__":
    # 请求路径
    url="https://movie.douban.com/j/chart/top_list"
    # 请求的参数
    param = {
        "type": "24",
        "interval_id": "100:90",
        "action":"",
        "start": "0",   # 从第几个电影开始取
        "limit": "20"    # 取出的个数
    }

    # User-Agent 伪装
    headers = {
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"
    }

    respone = requests.get(url=url, params=param, headers=headers)

    list_data = respone.json()
    print(list_data)

    fp = open("./douban.json", "w", encoding="utf-8")
    json.dump(list_data, fp=fp, ensure_ascii=False)
    print("complate...")