# 해보기_리스트 슬라이스
# 다양한 요소를 담고있는 리스트에 접근하여 필요한 자료 슬라이스 하기

listSlice = [1, 1.5, ['a', 'b', 'c', 'd'], 'AI', True, False]

print(listSlice[:])           # 전체
print(listSlice[1:4])         # 인덱스 1부터 3까지
print(listSlice[1:])          # 인덅�스 1부터 끝까지
print(listSlice[:4])          # 처음부터 인덱스 3까지
print(listSlice[2][1:3])      # 중첩 리스트 슬라이스
