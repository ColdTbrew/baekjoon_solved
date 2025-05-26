import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)

n = int(input())

dp = [float('inf')] * (n+1)
prev = [-1] * (n+1)
dp[1] = 0
for i in range(2, n+1):
    if dp[i-1] + 1 < dp[i]: # 최소인지 확인 
        dp[i] = dp[i-1]+1
        prev[i] = i-1
    if i%2==0 and dp[i//2] + 1 < dp[i]: # 나누어 떨어지는지 확인
        dp[i] = dp[i//2] + 1
        prev[i] = i//2 # 이전 경로 기록
    if i%3 == 0 and dp[i//3] + 1 < dp[i]: 
        dp[i] = dp[i//3] + 1
        prev[i] = i//3
ans = []
current = n
while current != -1:
    ans.append(current)
    current = prev[current]

print(dp[n])
print(*ans)