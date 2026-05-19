import pandas as pd

data = [
    ["노트북", 1200000, "전자제품"],
    ["키보드", 30000, "주변기기"],
    ["마우스", 15000, "주변기기"],
]

df = pd.DataFrame(data, columns=["상품명", "가격", "카테고리"])

print(df)
