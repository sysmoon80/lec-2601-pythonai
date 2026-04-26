scores = {
    "강호서": 90,
    "박천안": 95,
    "이당진": 84,
}

total = 0
for name, score in scores.items():
    total += score
    print("%s : %d" % (name, score))

print("합계 : %d, 평균 : %.2f" % (total, total / len(scores)))
