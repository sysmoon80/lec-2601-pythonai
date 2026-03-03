# 10주차 파일입출력 실습 3
# 텍스트 파일 한줄씩 읽어오기 (phones.txt 필요)

# 먼저 샘플 파일 생성
f = open("phones.txt", "w")
f.write("홍길동 010-1234-5678\n")
f.write("김철수 010-1234-5679\n")
f.write("김영희 010-1234-5680\n")
f.close()

# 한줄씩 읽어오기
f = open("phones.txt", "r")
line = f.readline()
while line != "":
    print(line)
    line = f.readline()
f.close()
