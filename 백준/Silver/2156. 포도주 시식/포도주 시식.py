import sys
input = sys.stdin.readline

N = int(input())
glass = []

for i in range(N):
    x = int(input())
    glass.append(x)

dp = [[0, 0, 0] for _ in range(N)]
#이전꺼랑 이전전꺼의 차이가 1이면 3잔 연속이됨
#dp[i][j]는 i번째 잔까지 고려했을때 j는 현재 잔을 마신 상태
#j=0 은 이번에 안먹음, j = 1 직전작은 안마시고 이번에 먹음, j = 2 직전잔과 이번잔 마심
max_num = 0
dp[0][1] = glass[0]

for i in range(1, N):
    g = glass[i]
    dp[i][0] = max(dp[i-1][0], dp[i-1][1], dp[i-1][2])
    dp[i][1] = dp[i-1][0] + g
    dp[i][2] = dp[i-1][1] + g

if N == 1:
    print(glass[0])
else:
    print(max(dp[N-1]))