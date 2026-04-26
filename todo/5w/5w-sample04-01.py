import turtle as t
m = int(input("그리고 싶은 다각형은? "))

t.Screen()
# 속도 1~10, 1이 가장 느리고 10이 가장 빠름
t.speed(1)

# shape() 함수는 거북이의 모양을 바꿔주는 함수입니다. 'turtle'은 거북이 모양입니다.
# 거북이 모양이 아닌 다른 모양도 사용할 수 있습니다. 예를 들어 'arrow'는 화살표 모양입니다.
t.shape('arrow')
t.pensize(5)

# 색상을 보라색으로 바꿔봅시다. 색상은 영어로 입력해야 합니다. 예를 들어 'red'는 빨간색입니다.
t.color('purple')

for i in range(m) :
    t.forward(100)
    t.left(360/m)
