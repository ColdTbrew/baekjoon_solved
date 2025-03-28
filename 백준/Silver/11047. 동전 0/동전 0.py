import sys
input = sys.stdin.readline

N, K = map(int, input().split())

coins = [[] for _ in range(N)]
for i in range(N):
    x = int(input().strip())
    coins[N-i-1] = x

# print(coins)

count = 0
for i in range(N):
    if coins[i] <= K:
        count += K // coins[i] 
        K %= coins[i]
        # print(K)
    if K == 0:
        break

print(count)