import sys
input = sys.stdin.readline

N = int(input())
a = list(map(int, input().split()))

M = int(input())

dp = [[0]*N for _ in range(N)]
for i in range(N):
    dp[i][i] = 1

for i in range(N-1):
    if a[i] == a[i+1]:
        dp[i][i+1] = 1

# print()
# print(*dp, sep='\n')

for length in range(3, N+1):
    for i in range(N-length + 1):
        j = i + length - 1
        if a[i] == a[j] and dp[i+1][j-1] == 1:
            dp[i][j] = 1

for _ in range(M):
    s, e = map(int, input().split())
    print(dp[s-1][e-1])