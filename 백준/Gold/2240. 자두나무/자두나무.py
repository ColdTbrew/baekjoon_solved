import sys
input = sys.stdin.readline

T, W = map(int, input().split())
plums = [0]

for i in range(T):
    x = int(input())
    plums.append(x)

#초기 조건 pos가 1, 2일때 w는 이동횟수일때 시간은 T일때 최대 자두 개수가 dp[t][w][pos]
dp = [[[0 for _ in range(3)] for _ in range(W+1)] for _ in range(T+1)]
dp[0][0][1] = 0
for t in range(1, T+1):
    for w in range(W+1):
        for pos in [1, 2]:
            if w == 0 and pos == 2:
                continue

            dp[t][w][pos]  = max(dp[t][w][pos], dp[t-1][w][pos] + (1 if plums[t] == pos else 0))
            #이동하는 경우
            if w < W:
                other_pos = 3- pos
                dp[t][w+1][other_pos] = max(dp[t][w+1][other_pos], dp[t-1][w][pos] + (1 if plums[t] == other_pos else 0))


ans = 0
for w in range(W+1):
    for pos in [1, 2]:
        ans = max(ans, dp[T][w][pos])

print(ans)