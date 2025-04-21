import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    k = int(input())
    n = int(input())
    # 1층 3호에 사려면 0층의 1호부터 3호까지의 사람들의 수의 ㅏㅎㅂ만큼 사람들을 데려와 살아야한다
    # 1층 3호 -> 0층의 1+ 2+ 3 = 6
    #     1호    2호    3호
    #0층   1명    2     3
    #1층   1     3     6
    #2층   1     4     10
    grid = [[0] * n for _ in range(k+1)]
    grid[0] = [x+1 for x in range(n)]

    for i in range(1, k+1):
        for j in range(n):
            x = 0
            for idx, lower in enumerate(grid[i-1]):
                if idx <= j:
                    x += lower
            grid[i][j] = x
    print(grid[k][n-1])