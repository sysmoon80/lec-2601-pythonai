# 해보기9 (3) - 햄버거집 키오스크 주문 집계 프로그램
# 조건: 메뉴와 가격은 딕셔너리에 저장, 주문 내역도 딕셔너리에 저장
#        0 입력시 주문 종료, 잘못된 메뉴 입력시 경고

menu = {
    1: {"name": "치즈버거", "price": 5500},
    2: {"name": "불고기버거", "price": 6000},
    3: {"name": "감자튀김", "price": 2500},
    4: {"name": "콜라", "price": 1500}
}
order = {}


def show_menu():
    print("\n[메뉴]")
    for num in menu:
        print(f"{num}. {menu[num]['name']}({menu[num]['price']}원)")
    print("0. 결제")


while True:
    show_menu()
    try:
        choice = int(input("메뉴 번호(0:결제): "))
    except:
        print("숫자로 입력하세요.")
        continue

    if choice == 0:
        break
    if choice not in menu:
        print("잘못된 메뉴입니다.")
        continue
    try:
        qty = int(input("수량: "))
    except:
        print("수량은 숫자로 입력하세요.")
        continue

    if qty < 1:
        print("수량은 1 이상이어야 합니다.")
        continue

    order[choice] = order.get(choice, 0) + qty
    print("추가 주문이 반영되었습니다.")

print("\n=== 주문 내역 ===")
total = 0
for num, qty in order.items():
    item_total = menu[num]['price'] * qty
    total += item_total
    print(f"{menu[num]['name']} {qty}개: {item_total:,}원")

print(f"\n총 결제 금액: {total:,}원")
