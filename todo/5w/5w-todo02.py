# 해보기_최대공약수 (1)
# 두 정수를 입력 받아 최대 공약수를 구하는 프로그램
# 알고리즘:
# 1) 최대공약수(gcd)와 반복카운터변수(step) 초기화 후 두 정수 입력
# 2) step이 두 정수보다 작은지 비교
# 3) 조건 만족 시 두 정수가 step으로 나눠지면 최대공약수 변경
# 4) 조건 만족하지 않을 때까지 반복
# 5) 조건 만족하지 않으면 현재 최대공약수 출력하고 종료

gcd, step = 1, 2
num1 = int(input('Enter the number1 : '))
num2 = int(input('Enter the number2 : '))

while (step <= num1) and (step <= num2):
    if (num1 % step == 0) and (num2 % step == 0):
        gcd = step
    step = step + 1

print('최대공약수 : ', gcd)
