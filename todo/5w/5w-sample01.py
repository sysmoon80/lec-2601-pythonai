# 프로그램 설명
# 1. 사용자로부터 숫자를 입력받는다.
# 2. 0부터 입력받은 숫자까지의 합계를 구한다.

n, step, total = 0, 0, 0
n = int(input('Enter the number : '))

while (step <= n):
    total = total + step
    step = step + 1
print('총 합계 : ', total)
