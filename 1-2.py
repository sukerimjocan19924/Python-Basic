import time
import requests

urls = ["http://www.daum.net", "http://www.naver.com", "http://www.inflearn.com"]

for url in urls:
    response = requests.get(url)

    print(response.status_code)

    time.sleep(1)
