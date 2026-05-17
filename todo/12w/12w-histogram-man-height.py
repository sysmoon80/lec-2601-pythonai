import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_excel("data/12w/health_screenings_2020_1000ea.xlsx")

mandata = data.loc[data.gender == 1.0, ["gender", "height"]]
plt.figure(figsize=(10, 6))
plt.hist(mandata["height"], bins=20, label="Man")
plt.xlim(140, 200)
plt.xlabel("height")
plt.ylabel("frequency")
plt.title("2020 Health Screenings Man Height Histogram")
plt.legend()
plt.grid()
plt.show()
