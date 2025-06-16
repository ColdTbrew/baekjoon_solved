import sys
input = sys.stdin.readline

N, K = map(int, input().split())
coin = []

dp = [0] * (K+1)
for _ in range(N):
    x = int(input())
    coin.append(x)
    

# dp i 는 i원일때 경우의수
dp[0] = 1

for c in coin:
    for j in range(c, K+1):
        dp[j] += dp[j-c]
    # print("coin ", c)
    # print(dp)
print(dp[K])