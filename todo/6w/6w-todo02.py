# 해보기_함수1
# 학점을 구하는 프로그램
# 두개의 점수를 입력받아 평균을 구하고, 함수를 호출하여 학점을 되돌려주는 프로그램 만들기

def grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

s1 = float(input("첫 번째 점수 입력: "))
s2 = float(input("두 번째 점수 입력: "))

avg = (s1 + s2) / 2
print("평균:", avg)
print("학점:", grade(avg))
