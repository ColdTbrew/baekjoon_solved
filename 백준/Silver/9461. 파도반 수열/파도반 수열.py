import sys
input = sys.stdin.readline

N = int(input().strip())

dp = [0] * 101
dp[1] = 1
dp[2] = 1
dp[3] = 1
dp[4] = 2
dp[5] = 2
dp[6] = 3
dp[7] = 4
dp[8] = 5
dp[9] = 7
for _ in range(N):
    n = int(input().strip())
    for i in range(4, n+1):
        dp[i] = dp[i-2]+ dp[i-3]
    print(dp[n])