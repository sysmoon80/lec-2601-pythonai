try:
    num = int(input("숫자를 입력하세요: "))
    result = 10 / num
    print("결과:", result)
except ZeroDivisionError:
    print("0으로 나눌 수 없습니다.")
except ValueError:
    print("숫자만 입력하세요.")
finally:
    print("프로그램 종료")
