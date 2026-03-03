# 해보기4 - 공부시간과 시험점수의 관계를 시각화 (산점도)
# 조건: 공부시간 [1,2,3,4,5,6], 시험점수 [50,55,65,70,80,90]
# 제목: 'study', x축: study, y축: score

import matplotlib.pyplot as plt

study_time = [1, 2, 3, 4, 5, 6]
scores = [50, 55, 65, 70, 80, 90]

plt.scatter(study_time, scores)
plt.title("study")
plt.xlabel("study")
plt.ylabel("score")
plt.show()
