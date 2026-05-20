from bs4 import BeautifulSoup

html = """
<a href="https://example.com">사이트 이동</a>
<img src="image.png">
"""
soup = BeautifulSoup(html, "html.parser")

link = soup.find("a")
image = soup.find("img")


print(link.get("href"))
print(image.get("src"))
