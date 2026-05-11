import pandas as pd

# 파일 읽기 (충남 평생교육 기관 정보 CSV)
df = pd.read_csv(
    "data/11w/(재개방 필요)충청남도 평생교육 기관 현황_20230824.csv", encoding="cp949"
)

region_count = df.groupby("지역")["기관명"].count()

total = region_count.sum()

result = pd.DataFrame(
    {"기관수": region_count, "비율(%)": (region_count / total * 100).round(2)}
)

result = result.sort_values(by="기관수", ascending=False)

print(result)
