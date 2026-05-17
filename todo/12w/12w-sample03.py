# (샘플3) 직선 그래프에 마커 지정하기

import matplotlib.pyplot as plt

plt.title("X Y range")
xdata = [10, 20, 30, 40]
ydata = [1, 3, 5, 7]
plt.plot(xdata, ydata, color="b", linestyle="--", marker="o", markersize="10")
plt.xlim(0, 50)
plt.ylim(-5, 15)
plt.show()
