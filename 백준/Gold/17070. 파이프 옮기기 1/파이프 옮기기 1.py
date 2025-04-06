N = int(input())
grid = [list(map(int, input().split())) for _ in range(N)]

# DP 배열: [행][열][방향] (0: 가로, 1: 세로, 2: 대각선)
dp = [[[0] * 3 for _ in range(N)] for _ in range(N)]

# 초기 상태: (1,1)-(1,2) 가로 -> 끝점 (1,2)
dp[0][1][0] = 1  # 0-based이므로 (0,1)

for j in range(2, N):
    if grid[0][j] == 0:
        dp[0][j][0] = dp[0][j-1][0]

# DP 채우기
for i in range(1, N):
    for j in range(1, N):
        if grid[i][j] == 0 and grid[i][j-1] == 0 and grid[i-1][j] == 0:
            dp[i][j][2] = dp[i-1][j-1][0] + dp[i-1][j-1][1] + dp[i-1][j-1][2]
        if grid[i][j] == 0:
            dp[i][j][0] = dp[i][j-1][0] + dp[i][j-1][2]
            dp[i][j][1] = dp[i-1][j][1] + dp[i-1][j][2]

# 결과: 끝점 (N,N)에 도달하는 모든 경우의 수
result = dp[N-1][N-1][0] + dp[N-1][N-1][1] + dp[N-1][N-1][2]
print(result)