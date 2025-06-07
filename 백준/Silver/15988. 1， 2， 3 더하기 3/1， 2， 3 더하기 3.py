import sys
input = sys.stdin.readline

T = int(input())

def solve(x):
    dp = [0] * (x+1)
    # dp i 는 정수 i를 1,2,3의 합으로 나타내는 방법이다.
    if x == 0:
        return 0
    if x == 1:
        return 1
    if x == 2:
        return 2
    dp[1] = 1
    dp[2] = 2
    dp[3] = 4
    for i in range(4, x+1):
        dp[i] = (dp[i-1] + dp[i-2] + dp[i-3])%(10**9+9)
    
    return dp[x]
for _ in range(T):
    x = int(input())
    print(solve(x))