import sys
input = sys.stdin.readline

N = int(input().strip())

for _ in range(N):
    n = int(input().strip())

    dp = [0] * (11+1)
    dp[1] = 1
    dp[2] = 2 #11 2
    dp[3] = 4 #111, 21,12, 3
    # dp[4] = 7  #7가지
    for i in range(4, n+1):
        dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
    
    print(dp[n])