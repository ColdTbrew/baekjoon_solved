import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)


N = int(input())

dp = [[0, 0] for _ in range(N+1)]
dp[1][0] = 0 
dp[1][1] = 1 # 이친수의 개수

# n = 2 : 10
# n = 3 : 101 , 100, 
# n = 4 : 1010, 1000, 1001

for i in range(2, N+1):
    dp[i][0] = dp[i-1][0] + dp[i-1][1] # 0으로 끝나려면 그전이 0 또는 1가능
    dp[i][1] = dp[i-1][0] # 1로 끝나려면 전이 무조건 0인거에서와야함

print(dp[N][0]+dp[N][1])