import requests

url = "http://www.daum.net"

response = requests.get(url)

response.encoding = "utf-8"

print(response.text)


# 웹 크롤링
