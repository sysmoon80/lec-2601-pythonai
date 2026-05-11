# 해보기11 (3)
# read_excel() 호출을 위해 uv add openpyxl 명령어로 openpyxl 패키지 설치 필요
# 충남 지역의 기상 데이터
# 지점명별 평균 기온, 총 강수량 구하기
# 평균 기온이 가장 높은 지점 출력하기

import pandas as pd

df = pd.read_excel("data/11w/weather.xlsx")

# 지점명별 평균 기온 (내림차순 정렬)
mean_temp = df.groupby("지점명")["기온(°C)"].mean().sort_values(ascending=False)

# 지점명별 총 강수량 (내림차순 정렬)
total_rain = df.groupby("지점명")["강수량(mm)"].sum().sort_values(ascending=False)

# 평균 기온이 가장 높은 지점
hottest_region = mean_temp.idxmax()
hottest_value = mean_temp.max()

print("=== 지점별 평균 기온 ===")
print(mean_temp)
print(f"\n평균 기온이 가장 높은 지점: {hottest_region} ({round(hottest_value, 2)}°C)")

print("\n=== 지점별 총 강수량 ===")
print(total_rain)
