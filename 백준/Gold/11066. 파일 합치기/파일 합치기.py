T = int(input())
for _ in range(T):
    N = int(input())
    costs = list(map(int, input().split()))

    prefix = [0] * (N+1)
    for i in range(1, N+1):
        prefix[i] = prefix[i-1] + costs[i-1]
    # print("미리 계산된 누적합 ", prefix)

    dp = [[0]* N for _ in range(N)]
    # 2차원 디비 dp[i][j]는 i부터 j까지의 합의 최소 코스트

    #길이가 2인거 부터 하는데
    for length in range(2, N+1):
        for i in range(0, N-length + 1):
            j = i + length - 1 # 0, 1부터
            dp[i][j] = float('inf')
            for k in range(i, j):
                cost = dp[i][k] + dp[k+1][j] + (prefix[j+1] - prefix[i])
                if cost < dp[i][j]:
                    dp[i][j] = cost
    
    # print(*dp, sep = "\n")
    print(dp[0][N-1])

