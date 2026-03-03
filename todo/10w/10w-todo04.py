# 10주차 파일입출력 실습 4
# 텍스트 파일 한줄씩 읽어오기2 - with 문 사용

# 먼저 샘플 파일 생성
with open("phones.txt", "w") as f:
    f.write("홍길동 010-1234-5678\n")
    f.write("김철수 010-1234-5679\n")
    f.write("김영희 010-1234-5680\n")

# with 문으로 읽기
with open("phones.txt", "r") as f:
    while True:
        line = f.readline()
        if not line:
            break
        print(line.strip())
