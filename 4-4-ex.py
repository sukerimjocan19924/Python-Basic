from bs4 import BeautifulSoup

html = """
<div class="product">
  <h2>무선 마우스</h2>
  <p class="price">15000원</p>
</div>
<div class="product">
  <h2>키보드</h2>
  <p class="price">30000원</p>
</div>
"""

soup = BeautifulSoup(html, "html.parser")


products = soup.select(".product")

result = []

for product in products:
    name = product.find("h2").text
    price = product.find("p", class_="price").text

    result.append({"상품명 : ": name, "가격": price})


print(result)
