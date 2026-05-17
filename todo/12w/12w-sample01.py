# (샘플1) 직선 그래프 그리기

import matplotlib.pyplot as plt
from pathlib import Path

X = ["Mon", "Tue", "Wed", "Thur", "Fri", "Sat", "Sun"]
Y = [15.6, 14.2, 16.3, 18.2, 17.1, 20.2, 22.4]
plt.plot(X, Y)
plt.show()

# save image to current directory
current_dir_path = Path(__file__).parent

plt.savefig(f"{current_dir_path}/image.png")
