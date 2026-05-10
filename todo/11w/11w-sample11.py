import pandas as pd
from pathlib import Path

csv_path = Path("data/11w/exam_nan.csv")

df = pd.read_csv(csv_path)
df_no_na = df.dropna()

print(df_no_na)
