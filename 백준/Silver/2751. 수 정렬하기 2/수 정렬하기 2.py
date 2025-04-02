import sys
input = sys.stdin.readline

N = int(input().strip())

nums = [int(input().strip()) for _ in range(N)]
print(*sorted(nums), sep = "\n")