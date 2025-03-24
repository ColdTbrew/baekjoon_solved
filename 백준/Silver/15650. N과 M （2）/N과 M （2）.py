import sys
input = sys.stdin.readline

n, m = map(int, input().split())
from itertools import permutations

hubo = []
for p in permutations(range(1, n+1), m):
    hubo.append(p)

ans = []
for h in hubo:
    last = 0
    is_ok = True
    for num in h:
        if num < last:
            is_ok = False
        last = num
    if is_ok and not h in ans:
        ans.append(h)

ans.sort()
for i in ans:
    print(*i)
