# 해보기_선형대수를 이용한 추천시스템
# 사용자 취향과 영화 장르 특성을 행렬곱으로 추천 점수 계산

import numpy as np

# [액션, 로맨스, 공포]
user_taste = np.array([
    [5, 1, 2],     # 철수 → 액션 좋아함
    [1, 5, 1],     # 영희 → 로맨스 좋아함
    [2, 1, 5]      # 민수 → 공포 좋아함
])

item_feature = np.array([
    [5, 1, 1],     # 액션영화
    [1, 5, 1],     # 로맨스영화
    [1, 1, 5]      # 공포영화
])

score = user_taste @ item_feature  # 추천 점수 계산
print(score)
