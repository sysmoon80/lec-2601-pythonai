# 해보기2 - 남자 키 데이터 히스토그램
# 2020 Health Screenings Man Height Histogram

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# 예시 데이터 생성 (실제로는 엑셀 파일에서 로드)
np.random.seed(42)
data = pd.DataFrame({
    'gender': np.random.choice([1.0, 2.0], 1000),  # 1.0: 남자, 2.0: 여자
    'height': np.random.normal(170, 10, 1000)
})

mandata = data.loc[data.gender == 1.0, ['gender', 'height']]

plt.figure(figsize=(10, 6))
plt.hist(mandata['height'], bins=20, label='Man')
plt.xlim(140, 200)
plt.xlabel('height')
plt.ylabel('frequency')
plt.title('2020 Health Screenings Man Height Histogram')
plt.legend()
plt.grid()
plt.show()
