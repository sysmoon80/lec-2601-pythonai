# 행맨(Hangman) 형태의 단어 맞추기 게임

import random

guesses = ""
turns = 10

# 단어 목록에서 정답 단어를 무작위 선택
infile = open("./data/10w/words.txt", "r")
lines = infile.readlines()
word = random.choice(lines).strip()

# 기회가 남아있는 동안 게임 반복
while turns > 0:
    failed = 0
    for char in word:
        if char in guesses:
            print(char, end="")
        else:
            print("_", end="")
            failed += 1

    # 단어를 모두 맞췄으면 승리 후 종료
    if failed == 0:
        print("\n사용자 승리")
        break

    print("")
    guess = input("단어를 추측하시오: ")
    guesses += guess

    # 오답이면 남은 기회 감소
    if guess not in word:
        turns -= 1
        print("틀렸음!")
        print(str(turns) + "기회가 남았음!")
        if turns == 0:
            print("사용자 패배 정답은 " + word)

# 파일 닫기
infile.close()
