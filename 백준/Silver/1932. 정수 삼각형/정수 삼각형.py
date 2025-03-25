import sys
input = sys.stdin.readline

# 입력
N = int(input().strip())
triangle = [[] for _ in range(N)]
for i in range(N):
    row = list(map(int, input().split()))
    triangle[i] = (row)

# print(triangle)

# DP 테이블: dp[i][j]는 (i, j)까지의 최대 합
dp = [[0] * (i+1) for i in range(N)]
dp[0][0] = triangle[0][0]

for i in range(1, N):
    for j in range(i+1):
        # 위 왼쪽 에서 옴
        if j > 0:
            dp[i][j] = max(dp[i][j], dp[i-1][j-1] + triangle[i][j])
        if j < i:
        # 위 오른쪽
            dp[i][j] = max(dp[i][j], dp[i-1][j] + triangle[i][j])

print(max(dp[N-1]))