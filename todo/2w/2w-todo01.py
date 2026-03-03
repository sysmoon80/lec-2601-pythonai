'''
문제:
아래 지시사항대로 변수를 만들고 각 값을 할당 하시오. 
국어점수 80, 수학점수 90, 영어점수 75
위 교과목의 점수의 합계와 평균을 구하시오. 

'''
# 교과목 점수 변수 할당
korean_score = 80
math_score = 90
english_score = 75

# 합계 계산
total_score = korean_score + math_score + english_score

# 평균 계산
average_score = total_score / 3

# 결과 출력
print(f"국어 점수: {korean_score}")
print(f"수학 점수: {math_score}")
print(f"영어 점수: {english_score}")
print(f"합계: {total_score}")
print(f"평균: {average_score}")
