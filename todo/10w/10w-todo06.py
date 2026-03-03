# 10주차 파일입출력 실습 6
# 텍스트 파일을 읽어서 각 라인을 출력 (with문 + for문)

# 먼저 샘플 파일 생성
with open("proverbs.txt", "w") as f:
    f.write("All's well that ends well.\n")
    f.write("Bad news travels fast.\n")
    f.write("Well begun is half done.\n")
    f.write("Birds of a feather flock together\n")

# with문과 for문으로 읽기
with open("proverbs.txt", "r") as file:
    for line in file:
        print(line.strip())
