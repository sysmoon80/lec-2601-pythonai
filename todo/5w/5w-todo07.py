# 해보기_별 그리기
# 사용자정의 '별' 그리기
# 단순한 다각형을 넘어 색이 채워지는 별 그리기
# begin_fill()과 end_fill() 삭제하고 그려보기

from turtle import *

shape("turtle")
color("gold")
begin_fill()

i = 0
while i < 5:
    forward(200)
    right(144)     # 별을 그리는 마법의 각도
    i = i + 1

end_fill()
done()
