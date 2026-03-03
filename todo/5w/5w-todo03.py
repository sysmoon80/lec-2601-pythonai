# 해보기_최대공약수 (2)
# 두 정수를 입력 받아 최대 공약수를 구하는 프로그램
# (슬라이드 28 버전)

gcd, step = 1, 2
num1 = int(input('Enter the number1 : '))
num2 = int(input('Enter the number2 : '))

while (step <= num1) and (step <= num2):
    if (num1 % step == 0) and (num2 % step == 0):
        gcd = step
    step = step + 1

print('최대공약수 : ', gcd)
