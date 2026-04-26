import numpy as np
data = np.array([10, 20, 30, 40, 50])

bool_index = np.array([True, False, True, False, True])
print(data)
print(data[bool_index])   # [10 30 50]     # 불리언 인덱싱
print(data[data > 25])    # [30 40 50]     # 조건식 필터링 
