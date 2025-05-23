import sys
input = sys.stdin.readline

N = 90
dp = [0] * (N+1)
dp[1] = 1
dp[2] = 1
dp[3] = 2
for i in range(3, N+1):
    dp[i] = dp[i-1] + dp[i-2]

x = int(input())
print(dp[x])