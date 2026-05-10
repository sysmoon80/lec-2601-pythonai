import pandas as pd

sales = pd.DataFrame(
    {
        "fruit": ["사과", "딸기", "수박"],
        "price": [1800, 1500, 3000],
        "volume": [24, 38, 13],
    }
)

print(sales)
