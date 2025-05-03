import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline

N = int(input())
dims = []

for _ in range(N):
    r, c = map(int, input().split())
    if not dims:
        dims.append(r)
    dims.append(c)

# DP 테이블 초기화: dp[i][j]는 i번째부터 j번째 행렬까지 곱하는 최소 연산 횟수
dp = [[float('inf')] * (N+1) for _ in range(N+1)]
for i in range(1, N+1):
    dp[i][i] = 0

for length in range(2, N+1): #길이는 2부터 N까지
    for i in range(1, N-length + 2): # i 는 1부터 N-length+1까지
        j = i+length -1 # j는 길이 만큼 더한 위치 -> 이놈이 N을 안넘는걸로 i 구간 결정
        for k in range(i, j):
            cost = dp[i][k] + dp[k+1][j] + dims[i-1] * dims[k] * dims[j]
            dp[i][j] = min(dp[i][j] , cost)
            # print(*dp, sep='\n')
            # print(f"i={i}, j={j}, k={k}, cost={cost}")

print(dp[1][N])
