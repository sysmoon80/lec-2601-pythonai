# 해보기_배열 (논리연산)
# scores 배열 중 70점 이상 90점 미만인 값만 선택하는 코드 완성하기

import numpy as np

scores = np.array([65, 70, 85, 90, 45])

selected = scores[(scores >= 70) & (scores < 90)]
print(selected)
