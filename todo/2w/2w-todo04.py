'''문제:
125초는 몇분 몇초인지 출력하는 프로그램을 작성하세요. 
'''
# 초 단위 시간
total_seconds = 125

# 분과 초로 변환
minutes = total_seconds // 60
seconds = total_seconds % 60

# 결과 출력
print(f"{total_seconds}초는 {minutes}분 {seconds}초입니다.")
