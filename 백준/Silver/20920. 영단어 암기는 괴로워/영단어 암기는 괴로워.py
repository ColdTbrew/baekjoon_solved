import sys
from collections import Counter

# 입력 처리
input = sys.stdin.readline
N, M = map(int, input().split())

# 단어 입력 및 빈도수 계산
words = [input().strip() for _ in range(N)]
word_count = Counter(word for word in words if len(word) >= M)

# 단어 리스트 생성: (단어, 빈도수)
word_list = [(word, count) for word, count in word_count.items()]

# 정렬: 1. 빈도수 내림차순(-count), 2. 길이 내림차순(-len(word)), 3. 사전순(word)
word_list.sort(key=lambda x: (-x[1], -len(x[0]), x[0]))

# 결과 출력
for word, _ in word_list:
    print(word)