# 해보기_함수2
# 상여금 구하기 프로그램
# 함수 2개를 작성하고 각각의 함수에서 나온 값을 더하기
# 알고리즘:
# - 사용자에게 급여와 직책을 입력받는다.
# - 함수1은 급여를 매개변수로 보내서 급여의 10%를 계산한다.
# - 함수2는 직책을 매개변수로 보내서 직책별 보너스를 계산한다.
# - 두 값을 반환하여 합계를 구한다.

def pay10x(pay):
    return pay * 0.1

def position_bonus(position):
    bonus_table = {
        "사원": 100000,
        "대리": 200000,
        "과장": 300000,
        "차장": 400000,
        "부장": 500000
    }
    return bonus_table.get(position, 0)  # 없는 직책이면 0원

pay = int(input("급여(원) 입력: "))
pos = input("직책 입력(사원/대리/과장/차장/부장): ").strip()

bonus = position_bonus(pos)
incentive = pay10x(pay)
total = pay + bonus + incentive

print(f"급여: {pay:,}원")
print(f"직책보너스: {bonus:,}원")
print(f"급여의 10%: {incentive:,.0f}원")
print("급여+인센티브 :", f"{total:,.0f}원")
