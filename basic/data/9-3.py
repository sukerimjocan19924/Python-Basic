import requests
import pandas as pd
from bs4 import BeautifulSoup

client_id = "aKdKF9ZPtuJ0hs_cctJd"
client_secret = "ZhYgPyJ1r7"

url = "https://openapi.naver.com/v1/search/blog.json"

headers = {"X-Naver-Client-Id": client_id, "X-Naver-Client-Secret": client_secret}

params = {"query": "파이썬", "display": 10, "start": 1, "sort": "sim"}

response = requests.get(url, headers=headers, params=params)

data = response.json()
rows = []

for item in data["items"]:
    rows.append(
        {
            "제목": BeautifulSoup(item["title"], "html.parser").get_text(),
            "링크": item["link"],
            "설명": BeautifulSoup(item["description"], "html.parser").get_text(),
            "블로그명": item["bloggername"],
            "작성일": item["postdate"],
        }
    )

df = pd.DataFrame(rows)
df.to_csv("naver_blog_result.csv", index=False, encoding="utf-8-sig")

print("CSV 작성 완료")
