# 10주차 파일입출력 실습 1
# 파일에 글 저장하기

f = open("test.txt", "w")
f.write("안녕하세요\n")
f.write("파일 저장 연습입니다.")
f.close()

print("파일 저장 완료!")
