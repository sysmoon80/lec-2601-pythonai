# 10주차 파일입출력 실습 7
# 파일에 데이터 쓰기 후 while문으로 읽기

# 데이터 쓰기
f = open("proverbs.txt", "w")
f.write("All's well that ends well.\n")
f.write("Bad news travels fast.\n")
f.write("Well begun is half done.\n")
f.write("Birds of a feather flock together\n")
f.close()

# while문으로 읽기
f = open("proverbs.txt", "r")
line = f.readline().rstrip()
while line != "":
    print(line)
    line = f.readline().rstrip()
f.close()
