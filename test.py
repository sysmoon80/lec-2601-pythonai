str = "89점"
try:
    score = int(str)
    print(score)
except Exception as e:
    print("예외가 발생했습니다.", e, type(e))
print("작업완료")
