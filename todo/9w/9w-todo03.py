# 해보기9 (3)
# 딕셔너리로 학생 정보 관리하기
# 조건: 공백 딕셔너리 생성, 최소 3명의 학생 정보 입력, 특정 학생 검색 기능

students = {}
for i in range(3):
    print(f"\n{i+1}번째 학생 정보 입력")
    name = input("이름: ")
    age = int(input("나이: "))
    major = input("전공: ")

    students[name] = {
        "나이": age,
        "전공": major
    }

print("\n=== 전체 학생 정보 ===")
for name, info in students.items():
    print("-----------------")
    print("이름:", name)
    print("나이:", info["나이"])
    print("전공:", info["전공"])

search_name = input("\n검색할 학생 이름을 입력하세요: ")

if search_name in students:
    print("\n=== 검색 결과 ===")
    print("이름:", search_name)
    print("나이:", students[search_name]["나이"])
    print("전공:", students[search_name]["전공"])
else:
    print("해당 학생 없음")
