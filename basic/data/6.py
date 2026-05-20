from bs4 import BeautifulSoup
import pandas as pd

html = """
<div class="movie">
  <h2 class="title"> 인터스텔라 </h2>
  <p class="rating">9.1점</p>
</div>
<div class="movie">
  <h2 class="title"> 기생충 </h2>
  <p class="rating">8.8점</p>
</div>
<div class="movie">
  <h2 class="title"> 범죄도시 </h2>
  <p class="rating">8.2점</p>
</div>
"""

soup = BeautifulSoup(html, "html.parser")

movies = []

for movie in soup.select(".movie"):
    title = movie.select_one(".title").text.strip()
    rating = movie.select_one(".rating").text.strip()

    movies.append({"영화제목": title, "별점": rating})

df = pd.DataFrame(movies)

df["별점"] = df["별점"].str.replace("점", "")
df["별점"] = df["별점"].astype(float)

df.to_csv("movies.csv", index=False, encoding="utf-8-sig")
df.to_excel("movies.xlsx", index=False)

print("데이터 저장 완료")
