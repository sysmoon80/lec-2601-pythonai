# 10주차 파일입출력 실습 2
# 텍스트 파일 불러오기

f = open("test.txt", "r")
data = f.read()
print(data)
f.close()
