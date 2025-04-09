import sys
input = sys.stdin.readline

N = int(input().strip())

array = []
for _ in range(N):
    T, P = map(int, input().split())
    array.append((T, P))

dp = [0] * (N+1)
for i in range(N-1, -1, -1):
    T, P = array[i]
    if i + T <= N:
        dp[i] = max(dp[i+1], P + dp[i+T])
    else:
        dp[i] = dp[i+1]
print(dp[0])