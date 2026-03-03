# 해보기11 (3)
# 충남 지역의 기상 데이터
# 지점명별 평균 기온, 총 강수량 구하기
# 평균 기온이 가장 높은 지점 출력하기

import pandas as pd

# 예시 데이터 생성 (실제로는 엑셀 파일에서 로드)
data = {
    '지점명': ['천안', '공주', '보령', '서산', '아산', '천안', '공주', '보령'],
    '기온(°C)': [15.5, 16.2, 14.8, 15.1, 16.5, 14.9, 15.8, 15.3],
    '강수량(mm)': [50, 45, 60, 55, 40, 52, 48, 58]
}

df = pd.DataFrame(data)

# 지점명별 평균 기온 (내림차순 정렬)
mean_temp = df.groupby('지점명')['기온(°C)'].mean().sort_values(ascending=False)

# 지점명별 총 강수량 (내림차순 정렬)
total_rain = df.groupby('지점명')['강수량(mm)'].sum().sort_values(ascending=False)

# 평균 기온이 가장 높은 지점
hottest_region = mean_temp.idxmax()
hottest_value = mean_temp.max()

print("=== 지점별 평균 기온 ===")
print(mean_temp)
print(f"\n평균 기온이 가장 높은 지점: {hottest_region} ({round(hottest_value, 2)}°C)")

print("\n=== 지점별 총 강수량 ===")
print(total_rain)
