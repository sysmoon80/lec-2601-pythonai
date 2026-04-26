fruits = {"apple": 5, "banana": 3, "orange": 2}
# 특정 키 삭제
del fruits["banana"]
print(fruits) # 출력: {'apple': 5, 'orange': 2}
# 특정 키를 삭제하면서 반환
removed_value = fruits.pop("apple")
print(removed_value)
print(fruits) # 출력: {''orange': 2} 