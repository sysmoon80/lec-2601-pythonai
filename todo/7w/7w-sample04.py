import numpy as np
point = np.array([2, 0])          # 원본 좌표

angle = np.radians(90)            # 90도 회전 
rotation_matrix = np.array([[np.cos(angle), -np.sin(angle)],
                             [np.sin(angle),  np.cos(angle)]])

new_point = rotation_matrix @ point   # 행렬 곱셈으로 새 좌표 계산

print(f"원본 좌표: {point}")       
print(f"회전 후 좌표: {np.round(new_point)}")
