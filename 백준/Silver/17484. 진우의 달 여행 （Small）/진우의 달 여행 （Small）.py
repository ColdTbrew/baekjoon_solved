N, M = map(int,input().split())
grid = []
for _ in range(N):
    row = list(map(int, input().split()))
    grid.append(row)

# dp 그리드 정의
dp = [[[float('inf') for _ in range(3)] for _ in range(M)] for _ in range(N)]
# 초기값 세팅
for j in range(M):
    for k in range(3):
        dp[0][j][k] = grid[0][j]

# print(dp)
for i in range(1, N):
    for j in range(M):
        # 0. 왼쪽 대각선 위에서 온 경우
        if j > 0:
            dp[i][j][0] = min(dp[i-1][j-1][1], dp[i-1][j-1][2]) + grid[i][j]
        # 1. 바로 위에서 온 경우
        dp[i][j][1] = min(dp[i-1][j][0], dp[i-1][j][2]) + grid[i][j]
        # 2. 오른쪽 위에서 온경우
        if j < M-1:
            dp[i][j][2] = min(dp[i-1][j+1][1],dp[i-1][j+1][0] ) + grid[i][j]
    
result = float('inf')
for j in range(M):
    result = min(result, min(dp[N-1][j]))
print(result)