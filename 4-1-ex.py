from bs4 import BeautifulSoup

html = """
<html>
  <body>
    <ul>
      <li class="item">Python</li>
      <li class="item">Java</li>
      <li class="item">JavaScript</li>
      <li>React</li>
    </ul>
  </body>
</html>
"""
soup = BeautifulSoup(html, "html.parser")

items = soup.find_all("li", class_="item")

for item in items:
    print(item.text)
