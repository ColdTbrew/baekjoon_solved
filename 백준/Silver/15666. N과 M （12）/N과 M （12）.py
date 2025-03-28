import sys
input = sys.stdin.readline

N, M = map(int, input().split())


nums = list(map(int,input().split()))


from itertools import combinations_with_replacement

nums.sort()
result = set()
for outs in combinations_with_replacement(nums, M):
    if outs not in result:
        print(*outs)
        result.add(outs)
    