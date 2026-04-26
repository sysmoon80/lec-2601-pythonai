scores = {
    "강호서": 95,
    "박천안": 88,
    "이당진": 76,
    "최창업": 90,
    "김아산": 82,
}

print("📌 장학금 대상자 판별 결과")

for name in scores:
    score = scores[name]
    if score >= 90:
        print(f"{name} : {score}점 → 우수 장학금 대상")
    elif score >= 80:
        print(f"{name} : {score}점 → 격려 장학금 대상")
    else:
        print(f"{name} : {score}점 → 장학금 대상 아님")
