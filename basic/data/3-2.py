import requests
from bs4 import BeautifulSoup

url = "https://www.work24.go.kr/"

response = requests.get(url)
html = response.text

soup = BeautifulSoup(html, "html.parser")

title = soup.find("h2")
content = soup.find("p")
link = soup.find("a")

print(title.text)
print(content.text)
print(link["href"])

# BeautifulSoup이용
