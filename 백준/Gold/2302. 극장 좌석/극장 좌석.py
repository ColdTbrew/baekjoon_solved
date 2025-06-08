import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
vips = []
for _ in range(M):
    x = int(input())
    vips.append(x)

groups = []
prev = 0
for vip in vips:
    length = vip - prev - 1
    if length > 0:
        groups.append(length)
    groups.append(1)
    prev = vip

if prev < N:
    groups.append( N- prev)

dp = [0] * (N+1)
# dp i 는 길이가 i일때의 가능한 조합개수
dp[0] = 1
dp[1] = 1
if N>=2:
    dp[2] = 2
for i in range(3, N+1):
    dp[i] = dp[i-1] + dp[i-2]

ans = 1
for len in groups:
    ans *= dp[len]

print(ans)

# 1 2 3 4
# 2 1 3 4
# 1 3 2 4
# 1 2 4 3
# 2 1 4 3
