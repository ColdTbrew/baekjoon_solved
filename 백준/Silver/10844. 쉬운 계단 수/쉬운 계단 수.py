import sys
input = sys.stdin.readline

N = int(input())
dp = [[0] * 10 for _ in range(N+1)]
#길이가 n일때 각 자리로 끝나는 계단수의 개수

#길이가 1인 계단수는 각 숫자로 끝나는건 1개씩 있음
# 1,2,3,4,5,, 9, 0은 안됨
for j in range(1, 10):
    dp[1][j] = 1

for i in range(2, N+1):
    for j in range(0, 10):
        if j == 0:
            dp[i][j] = dp[i-1][1]
        elif j == 9:
            dp[i][j] = dp[i-1][8]
        else:
            dp[i][j] = dp[i-1][j-1]+ dp[i-1][j+1]
        dp[i][j] %= 10**9

print(sum(dp[N]) % 10**9)
