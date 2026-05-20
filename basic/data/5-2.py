import pandas as pd

data = {
    "상품명": ["노트북", "키보드", "마우스"],
    "가격": [1200000, 30000, 15000],
    "카테고리": ["전자제품", "주변기기", "주변기기"],
}

df = pd.DataFrame(data)

print(df)
