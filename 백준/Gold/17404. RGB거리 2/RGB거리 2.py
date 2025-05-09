import sys
input = sys.stdin.readline

N = int(input())
# 인접집과 색이 달라야하고
# 1, N번째 집의 색은 달라야한다
# dp[i] 는 i번째 집에서의 최소 비용
houses = [list(map(int, input().split())) for _ in range(N)]
pos = [0] * (N+1) #R, G, B : 0, 1, 2
result = float('inf')
for first_color in range(3):
    dp = [[float('inf')]*3 for _ in range(N)]

    #첫 컬러의 비용 넣기
    dp[0][first_color] = houses[0][first_color]
    
    for i in range(1, N):
        dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + houses[i][0] #R
        dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + houses[i][1] #G
        dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + houses[i][2] #B
    
    #마지막 집선택
    for last_color in range(3):
        if last_color != first_color:
            result = min(result, dp[N-1][last_color])

print(result)