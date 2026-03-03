# 10주차 파일입출력 실습 5
# 텍스트 파일 한줄씩 읽어오기3 - readlines() 사용

# 먼저 샘플 파일 생성
with open("phones.txt", "w") as f:
    f.write("홍길동 010-1234-5678\n")
    f.write("김철수 010-1234-5679\n")
    f.write("김영희 010-1234-5680\n")

# readlines()로 읽기
with open("phones.txt", "r") as f:
    lines = f.readlines()
    print(lines)

# 각 라인 출력
print("\n=== 각 라인 출력 ===")
with open("phones.txt", "r") as f:
    for line in f:
        print(line.strip())
