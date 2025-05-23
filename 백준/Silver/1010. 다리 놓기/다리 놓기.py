import sys
input = sys.stdin.readline

# 최대 M, N이 30이므로 미리 DP 테이블 생성
MAX_M = 30
dp = [[0] * (MAX_M + 1) for _ in range(MAX_M + 1)]

# 초기화: dp[i][0] = 1, dp[i][i] = 1
for i in range(MAX_M + 1):
    dp[i][0] = 1
    dp[i][i] = 1

# DP 테이블 채우기: dp[i][j] = i개에서 j개를 선택하는 경우의 수
for i in range(1, MAX_M + 1):
    for j in range(1, i):
        dp[i][j] = dp[i-1][j-1] + dp[i-1][j]

# 테스트 케이스 처리
T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    print(dp[M][N])