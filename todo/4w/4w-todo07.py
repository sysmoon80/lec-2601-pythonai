#!/usr/bin/env python3
"""
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
해보기 7: 'a'가 포함된 과일 찾기 (문자열 검색)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

【문제】
과일 리스트에서 'a'가 포함된 과일만 찾아 새 리스트에 저장하시오.

【조건】
- 과일 리스트: ["apple", "banana", "cherry", "kiwi", "melon"]
- 'a'가 포함된 과일 리스트: a_fruits = []
- in 연산자 사용하여 문자열 포함 여부 확인

【실행 예시】
결과 리스트: ['apple', 'banana', 'orange']
"""

# 과일 리스트
fruits = ["apple", "banana", "cherry", "kiwi", "melon", "orange"]

# 'a'가 포함된 과일 리스트
a_fruits = []

# 'a'가 포함된 과일 찾기
for f in fruits:
    if 'a' in f:
        a_fruits.append(f)

print(f"결과 리스트: {a_fruits}")
