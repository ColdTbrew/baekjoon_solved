def solution(matrix_sizes):
    n = len(matrix_sizes)
    if n <= 1:
        return 0
    
    # 차원 배열 추출
    sizes = [matrix_sizes[i][0] for i in range(n)] + [matrix_sizes[-1][1]]
    print(sizes)
    
    dp = [[0] * n for _ in range(n)]
    print(dp)
    
    for length in range(2, n+1):
        for i in range(0, n-length + 1):
            j = i + length - 1
            dp[i][j] = float('inf')
            for k in range(i, j):
                # print("i , j, k", i, j, k)
                cost = dp[i][k] + dp[k+1][j] + sizes[i] * sizes[k+1] * sizes[j+1]
                if cost < dp[i][j]:
                    dp[i][j] = cost
    return dp[0][n-1]