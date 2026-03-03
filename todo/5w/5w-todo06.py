# 해보기_무지개색 나선형
# 선을 그릴 때마다 색상과 굵기를 바꿔주고, 어긋난 각도로 예술적인 나선형 그리기
# 리스트에 여러 색상을 담아두고, 선을 그을 때마다 선택하여 그리기

from turtle import *

speed(0)
colors = ["red", "orange", "yellow", "green", "blue", "purple"]

length = 5
i = 0
while i < 100:
    pencolor(colors[i % 6])  # 리스트 안의 색상을 번갈아 선택
    pensize(i / 10 + 1)      # 선이 점점 두꺼워짐
    forward(length)
    left(59)                 # 살짝 어긋난 각도로 나선형 생성
    length = length + 3      # 선이 점점 길어짐
    i = i + 1
