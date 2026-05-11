import pandas as pd

# 파일 읽기 (충남 평생교육 기관 정보 CSV)
df = pd.read_csv(
    "data/11w/(재개방 필요)충청남도 평생교육 기관 현황_20230824.csv", encoding="cp949"
)

# 데이터 살펴보기
print(df.head())
print(df.info())

# describe()로 기본 통계 정보 확인
print(df.describe())

# describe()로 모든 컬럼 포함해서 통계 정보 확인
print(df.describe(include="all"))

# 또는 특정 열만 선택해서 describe
print(df[["지역", "기관명"]].describe(include="all"))

# 충청남도 지역별 평생교육 기관 수 확인
print("\n=== 지역별 평생교육 기관 수: ===")
region_counts = df.groupby("지역")["기관명"].count()
print(region_counts)

# 지역별 전화번호 개수 확인
print("\n=== 지역별 전화번호 개수: ===")
phone_counts = df.groupby("지역")["전화번호"].count()
print(phone_counts)
