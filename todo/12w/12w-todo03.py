# 해보기3 - 학생 5명의 국어 점수를 이용하여 막대 그래프 그리기
# 조건: A:85점, B:90점, C:78점, D:92점, E:88점
# 제목: 'kor score', x축: student, y축: score

import matplotlib.pyplot as plt

students = ['A', 'B', 'C', 'D', 'E']
scores = [85, 90, 78, 92, 88]

plt.bar(students, scores)
plt.title("kor score")
plt.xlabel("student")
plt.ylabel("score")
plt.show()
