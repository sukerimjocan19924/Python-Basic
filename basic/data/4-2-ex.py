from bs4 import BeautifulSoup

html = """
<html>
  <body>
    <div class="news">
      <h2>첫 번째 뉴스</h2>
      <h2>두 번째 뉴스</h2>
      <h2>세 번째 뉴스</h2>
      <h3>네 번째 뉴스</h3>
    </div>
  </body>
</html>
"""

soup = BeautifulSoup(html, "html.parser")

news_titles = soup.select(".news h2")

for title in news_titles:
    print(title.text)
