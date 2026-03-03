# 해보기_학급 성적표 분석2
# 학생별 [국어, 영어, 수학] 점수 배열 분석

import numpy as np

grades = np.array([
    [80, 70, 80],
    [70, 65, 80],
    [100, 65, 90]
])

subject_avg = grades.mean(axis=0)              # 과목별 평균 (열 단위)
print(f"과목별 평균: {subject_avg}")

student_avg = grades.mean(axis=1)              # 학생별 평균 (행 단위)
print(f"학생별 평균: {student_avg}")

smart_students = grades[student_avg >= 80]     # 평균 80점 이상인 학생 필터링
print(f"80점 이상인 학생 점수 : {smart_students}")
