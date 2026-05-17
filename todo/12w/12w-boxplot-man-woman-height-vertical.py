import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data = pd.read_excel("data/12w/health_screenings_2020_1000ea.xlsx")

mandata = data.loc[data.gender == 1.0, ["gender", "height"]]
womandata = data.loc[data.gender == 2.0, ["gender", "height"]]

male = np.array(mandata["height"])
female = np.array(womandata["height"])

plt.figure(figsize=(8, 5))
plt.boxplot([male, female], labels=["Man", "Woman"])

plt.ylim(120, 200)
plt.xlabel("gender")
plt.ylabel("height")
plt.title("2020 Health Screenings Man & woman Height Box Plot")
plt.show()
