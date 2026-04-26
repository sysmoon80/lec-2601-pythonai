words = {
    "사과": "apple",
    "컴퓨터": "computer",
    "학교": "school",
    "책상": "desk",
    "의자": "chair",
}

print("-> 실행 결과")

for i in words.keys():
    answer = input("%s에 해당하는 영어 단어를 입력해 주세요 : " % i)
    if answer == words[i]:
        print("정답입니다!")
    else:
        print("틀렸습니다!")
