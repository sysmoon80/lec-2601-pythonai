import pandas as pd
from pathlib import Path

project_root = Path(__file__).resolve().parents[2]
csv_path = project_root / "data" / "11w" / "exam_nan.csv"

total_score = 0.0
valid_count = 0
student_count = 0

exam = pd.read_csv(csv_path)
student_count = exam["id"].count()

for _, row in exam.iterrows():
    student_name = f"학생{int(row['id'])}"
    score = row["math"]

    if pd.isna(score):
        print(f"{student_name}: 점수 없음(NaN)")
        continue

    print(f"{student_name}: {score}")

total_score = exam["math"].sum()
valid_count = exam["math"].count()
average_score = exam["math"].mean()

print("-" * 30)
print(f"전체 학생 수: {student_count}")
print(f"점수 집계 인원수: {valid_count}")
print(f"총합: {total_score}")
print(f"평균: {average_score:.2f}")
