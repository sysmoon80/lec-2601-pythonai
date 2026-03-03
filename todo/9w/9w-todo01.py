# 해보기9 (1)
# 사람들의 이름과 전화번호를 딕셔너리로 저장하여 추출하기
# 조건: 딕셔너리 이름은 contacts={}, 5개의 이름과 전화번호 넣기

contacts = {}
for i in range(5):
    key = input("이름을 입력: ")
    value = input("전화번호를 입력: ")
    contacts[key] = value

print("\n저장된 연락처:")
print(contacts)
