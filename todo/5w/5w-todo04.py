# 해보기_최대공약수 (3)
# math 라이브러리를 사용하면 한 줄에 처리 가능

import math

num1 = int(input('Enter the number1 : '))
num2 = int(input('Enter the number2 : '))

result = math.gcd(num1, num2)
print(f'{num1}와 {num2}의 최대공약수는 {result}')
