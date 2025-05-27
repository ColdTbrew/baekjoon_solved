import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)

n = int(input())

T = []
P = []
for i in range(n):
    t, p = map(int, input().split())
    T.append(t)
    P.append(p)

dp = [0] * (n+1)

for i in range(n-1, -1, -1):
    t, p = T[i], P[i]
    if i + t <= n: # 상담이 n일 이내에 끝나면
        dp[i] = max(dp[i+1], p+dp[i+t]) # 상담을 안하는 경우, i에 상담하고 i+t부터의 최대 수익
    else:
        dp[i] = dp[i+1]

print(dp[0])
