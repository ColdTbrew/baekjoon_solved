import sys
input = sys.stdin.readline

M = int(input())
mod = 1000000007
sum = 0
for _ in range(M):
    N, S = map(int, input().split())
    # N면체 주사위이고 모든 면의 적힌걸 더한값이 S
    # S/ N mod 1000000007
    inverse = pow(N, -1, mod)
    sum += (S*inverse) % mod
    sum = sum%mod
print(sum)