import sys
input = sys.stdin.readline

N = int(input().strip())
# dp[n] 은 2*n일때의 직사각형을 두는 방법의 개수
dp = [0] * (1000+1)
dp[1] = 1
dp[2] = 2
dp[3] = 3 # 2*3
dp[4] = dp[2] + dp[3]

for n in range(3, N+1):
    dp[n] = (dp[n-1] + dp[n-2])%10007
    

print(dp[N])