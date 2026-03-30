import turtle as t
m = int(input("그리고 싶은 다각형은? "))

t.Screen()
t.shape('turtle')
t.pensize(5)
t.color('blue')

for i in range(m) :
    t.forward(100)
    t.left(360/m)
