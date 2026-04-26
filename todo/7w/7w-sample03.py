import numpy as np
scores = np.array([65,70,85,90,45])

selected = scores[(scores >=70) & (scores <90)]
print(selected)
