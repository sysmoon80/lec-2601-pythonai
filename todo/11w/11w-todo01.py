# 해보기11 (1)
# 프로필(profile) 시리즈 객체 변수 나이에 대한 데이터가 20세 이상 24세 미만 결과 반환하기
# 조건: 두 개의 조건을 사용할 경우 각 조건을 ( )로 묶은 후 & 연산자를 이용하여 연결

import pandas as pd

name = ['홍길동', '김유신', '강감찬', '라이온', '유관순']
age = [20, 22, 21, 19, 24]

profile = pd.Series(age, index=name)
result = profile[(profile >= 20) & (profile < 24)]

print("원본 데이터:")
print(profile)
print("\n20세 이상 24세 미만:")
print(result)
