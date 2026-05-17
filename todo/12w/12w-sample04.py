# (샘플4) 직선 그래프 속성값 사용하기

import matplotlib.pyplot as plt
import pandas as pd

score = [
    [60, 90, 96],
    [80, 75, 100],
    [65, 85, 90],
    [85, 70, 90],
    [95, 90, 85],
    [75, 85, 90],
    [85, 80, 75],
]
subject = ["kor", "math", "eng"]

df = pd.DataFrame(score, columns=subject)
df.plot(kind="line")
plt.show()
