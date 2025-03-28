import sys
input = sys.stdin.readline

N, K = map(int, input().split())

wallet = {}

for _ in range(N):
    x, y = input().split()
    wallet[x] = y

for _ in range(K):
    x = input().strip()
    print(wallet[x])