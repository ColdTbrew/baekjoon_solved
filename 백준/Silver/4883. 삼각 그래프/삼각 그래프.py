t = 1
cost = 0
while 1:
    N = int(input())
    if N == 0:
        exit(0)
    graph = []
    for _ in range(N):
        row = list(map(int, input().split()))
        graph.append(row)
    dp = [[0] * 3 for _ in range(N)]
    dp[0][0] = float('inf')
    dp[0][1] = graph[0][1]
    dp[0][2] = graph[0][1] + graph[0][2]
    # print(dp)
    for i in range(1,N):
        dp[i][0] = graph[i][0] + min(dp[i-1][0],dp[i-1][1])
        dp[i][1] = graph[i][1] + min(dp[i-1][0],dp[i-1][1],dp[i-1][2],dp[i][0])
        dp[i][2] = graph[i][2] + min(dp[i-1][1],dp[i-1][2],dp[i][1])
    # print(dp)


    print("{}.".format(int(t)),dp[N-1][1])
    t += 1
