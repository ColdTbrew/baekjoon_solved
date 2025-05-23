import sys
input = sys.stdin.readline

N = 1000
dp = [0] * (N + 1)
dp[1] = 1  # SK 승
dp[2] = 0  # CY 승
dp[3] = 1  # SK 승

# DP 점화식: dp[i]는 i개 돌에서 SK가 이기는지(1) 또는 CY가 이기는지(0)
for i in range(4, N + 1):
    dp[i] = 1 if dp[i-1] == 0 or dp[i-3] == 0 else 0

x = int(input())
print("SK" if dp[x] == 1 else "CY")