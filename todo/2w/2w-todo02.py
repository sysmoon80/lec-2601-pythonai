'''
문제:
아래 반지름을 사용하여 원의 둘레와 원의 넓이를 구하시오. 
ㅇ 원주율 : 3.141592
ㅇ 반지름 : 7
 (원의 둘레 공식 : 2πr , 원의 넓이 공식 :       )
'''

# 변수 할당
pi = 3.141592
radius = 7

# 원의 둘레 계산 (2πr)
circumference = 2 * pi * radius

# 원의 넓이 계산 (πr²)
area = pi * radius ** 2

# 결과 출력
print(f"원주율: {pi}")
print(f"반지름: {radius}")
print(f"원의 둘레: {circumference}")
print(f"원의 넓이: {area}")
