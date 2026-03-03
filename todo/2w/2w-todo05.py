"""
문제:
f-string을 활용한 성적표 출력 print()문을 완성하시오. 
kor = 90, eng = 85, math = 80  점수가 주어졌을때, 세 과목의 합계와 평균을 계산하여 출력미리보기와 같은 형식으로 출력하세요.
"""

# 교과목 점수
kor = 90
eng = 85
math = 80

# 합계와 평균 계산
total = kor + eng + math
average = total / 3

# f-string을 활용한 성적표 출력
print(f"국어: {kor}점")
print(f"영어: {eng}점")
print(f"수학: {math}점")
print(f"합계: {total}점")
print(f"평균: {average:.2f}점")
