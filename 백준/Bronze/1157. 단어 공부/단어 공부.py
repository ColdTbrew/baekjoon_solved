import sys
from collections import Counter

# 입력 처리
word = input().strip().upper()  # 대문자 변환
word_c = Counter(word)  # 문자 빈도 계산

# 최대 빈도 찾기
max_count = max(word_c.values())  # 최대 빈도 수
max_chars = [char for char, count in word_c.items() if count == max_count]  # 최대 빈도 문자 리스트

# 출력: 최대 빈도 문자가 2개 이상이면 "?", 아니면 문자 출력
print("?" if len(max_chars) > 1 else max_chars[0])