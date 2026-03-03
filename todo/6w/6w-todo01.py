# 해보기_과일가격 계산
# 과일 가격 계산(입력값과 리턴값이 있는 함수)
# pineapple 가격이 개당 7천원일 때, 3개를 구입한다면 가격은 얼마인가?

# 함수정의
def price(num):  # num=3
    price_pineapple = 7000
    total_price = num * price_pineapple
    return total_price

# 함수호출
result = price(3)
print(result)
