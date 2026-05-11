import pandas as pd

accident = pd.read_csv("data/11w/acci.csv", encoding="CP949")
# print(accident)

print(accident.describe(include="all"))
