n = int(input())
cards = list(map(int, input().split()))
m = int(input())
have = list(map(int, input().split()))

counts = []
from collections import Counter
cards_count = Counter(cards)
# print(cards_count)
for h in have:
    counts.append(cards_count[h])

print(*counts, end= ' ')
"""
10
6 3 2 10 10 10 -10 -10 7 3
8
10 9 -5 2 3 4 5 -10
"""