import csv
from bs4 import BeautifulSoup

html = """
<html>
  <body>
    <div class="product">
      <h2 class="name">노트북</h2>
      <p class="price">1200000원</p>
    </div>

    <div class="product">
      <h2 class="name">태블릿</h2>
      <p class="price">600000원</p>
    </div>

    <div class="product">
      <h2 class="name">스마트폰</h2>
      <p class="price">900000원</p>
    </div>
  </body>
</html>
"""

soup = BeautifulSoup(html, "html.parser")

products = soup.select(".product")

data = []


for product in products:
    name = product.select_one(".name").text
    price = product.select_one(".price").text

    data.append([name, price])

with open("product.csv", "w", newline="", encoding="utf-8-sig") as file:
    writer = csv.writer(file)

    writer.writerow(["상품명", "가격"])

    writer.writerow(data)
