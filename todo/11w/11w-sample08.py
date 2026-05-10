import pandas as pd
from pathlib import Path

df_midterm = pd.DataFrame(
    {"english": [90, 80, 60, 70], "math": [50, 60, 100, 20], "nclass": [1, 1, 2, 2]}
)

base_dir = Path(__file__).resolve().parent
csv_path = base_dir / "output_newdata.csv"

df_midterm.to_csv(csv_path)
df_csv_exam = pd.read_csv(csv_path)
print(df_csv_exam)
