import sys
input = sys.stdin.readline

x = int(input().strip())

dp = [float('inf') for _ in range(10**6+1)]
# print(dp)
# dp[i] 는 숫자 i를 1로 만드는 데 필요한 최소 연산 횟수
dp[1] = 0
dp[2] = 1
if x not in [1,2]:    
    for i in range(3, x+1):
        a = float('inf')
        b = float('inf')
        if i%2 == 0:
            a = dp[i//2]+1
        if i%3 == 0:
            b = dp[i//3]+1
        dp[i] = min(dp[i-1]+1, a, b)

print(dp[x])