import sys
input = sys.stdin.readline

n = int(input().strip())

# dp[i]는 i를 표현하는 최소 제곱수 개수
dp = [float('inf')] * (n + 1)  # 무한대로 초기화
dp[0] = 0  # 0은 제곱수 0개

# 가능한 제곱수 목록 생성
squares = [i * i for i in range(1, int(n ** 0.5) + 1)]

# DP 계산
for sq in squares:
    for i in range(sq, n + 1):
        dp[i] = min(dp[i], dp[i - sq] + 1)
print(dp[n])