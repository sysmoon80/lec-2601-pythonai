# 해보기9 (2)
# 영한 사전 만들기
# 사용자로부터 영어 단어를 입력받아, 미리 저장된 영어-한국어 사전에서 해당 단어의 뜻을 찾아 출력

english_dict = dict()
english_dict['one'] = '하나'
english_dict['two'] = '둘'
english_dict['three'] = '셋'

word = input("단어를 입력하시오: ")
print(english_dict.get(word, "없음"))
