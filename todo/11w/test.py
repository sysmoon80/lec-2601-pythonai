import pandas as pd

df = pd.read_csv("data/11w/exam_nan.csv")

# score 결측치 제거
df_nomiss = df.dropna(subset="math")

print(df)
print(df_nomiss)
