import sys
input = sys.stdin.readline

N, M = map(int, input().split())
hubo = list(map(int, input().split()))
hubo.sort()
from itertools import permutations

outs = set()

for out in permutations(hubo, M):
    if out not in outs:
        outs.add(out)
        print(*out)
