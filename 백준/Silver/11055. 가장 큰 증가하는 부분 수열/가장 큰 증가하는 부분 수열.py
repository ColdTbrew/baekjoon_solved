import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)

n = int(input())
array = list(map(int, input().split()))
dp = [i for i in array]

for i in range(n):
    for j in range(i):
        if array[j] < array[i]: # 이전에 작은게 있으면
            dp[i] = max(dp[i], array[i] + dp[j])

print(max(dp))