import sys
input = sys.stdin.readline

N = int(input())
dp = [-1] * (N + 1)  # 불가능한 경우를 -1로 초기화

# 초기화
dp[0] = 0
if N >= 1: dp[1] = -1
if N >= 2: dp[2] = 1
if N >= 3: dp[3] = -1
if N >= 4: dp[4] = 2
if N >= 5: dp[5] = 1

# DP 계산
for i in range(6, N + 1):
    if dp[i-2] != -1 and dp[i-5] != -1:
        dp[i] = min(dp[i-2] + 1, dp[i-5] + 1)
    elif dp[i-2] != -1:
        dp[i] = dp[i-2] + 1
    elif dp[i-5] != -1:
        dp[i] = dp[i-5] + 1

print(dp[N])