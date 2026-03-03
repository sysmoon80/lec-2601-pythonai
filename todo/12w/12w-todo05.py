# 해보기5 - 어떤 반 학생들의 키 데이터를 가지고 히스토그램으로 표현
# 조건: 데이터 [160,162,165,170,172,168,174,169,171,163,167]
# 제목: 'student height', 구간(bin): 5개

import matplotlib.pyplot as plt

heights = [160, 162, 165, 170, 172, 168, 174, 169, 171, 163, 167]

plt.hist(heights, bins=5)
plt.title("student height")
plt.xlabel("height (cm)")
plt.ylabel("frequency")
plt.show()
