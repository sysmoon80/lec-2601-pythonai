# 해보기_배열2 (비교연산)
# 3보다 큰 값인지 비교하고, 배열 중 5이상만 추출

import numpy as np

a = np.array([1, 2, 3, 4, 5, 6, 7])

print(a > 3)
print(a[a >= 5])
