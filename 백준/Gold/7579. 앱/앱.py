import sys
input = sys.stdin.readline

#N개의 앱, M바이트의 메모리 필요
N, M = map(int, input().split())
active = list(map(int, input().split()))
cost = list(map(int, input().split()))

#cost의 합을 최소화 해서 M까지 만들어야함
max_cost = sum(cost)
dp = [0] * (max_cost+1) # dp[j] : 비용 j로 확보한 최대 메모리

# 각앱에서 비용별 최대 메모리 갱신
for i in range(N):
    m, c = active[i], cost[i]
    # 비용 j 를 역순으로 갱신 
    for j in range(max_cost, c-1, -1):
        dp[j] = max(dp[j] , dp[j-c] + m)

# 최소 비용찾기
for i in range(max_cost+1):
    if dp[i] >= M:
        print(i)
        break