# 해보기_회전하는 다각형 패턴
# 사각형을 10도 간격으로 36개 그리기
# 하나의 다각형을 그린 뒤, 거북이를 살짝 회전시켜 다시 그리기를 반복

from turtle import *

speed(0)
color("purple")

count = 0
while count < 36:        # 36번 반복하여 한 바퀴 돌기
    i = 0
    while i < 4:
        forward(100)
        right(90)
        i = i + 1
    right(10)            # 사각형 하나를 그린 후 10도 회전
    count = count + 1
