import sys
input = sys.stdin.readline

N = int(input()) # N개를 갖기 위한 금액의 최대값

dp = [[0] * 10 for _ in range(N+1)]
for j in range(10):
    dp[1][j] = 1

for i in range(2, N+1):
    for j in range(10):
        temp = 0
        #i번째 자리가 j일 때, 
        #i-1번째 자리는 j 이하의 숫자(0부터 j까지)여야 오르막 수 조건을 만족
        for k in range(j+1):
            temp += dp[i-1][k]
        dp[i][j] = temp % 10007

ans = 0
for j in range(10):
    ans+=dp[N][j]

print(ans%10007)