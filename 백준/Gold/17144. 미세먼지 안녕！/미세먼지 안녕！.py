import sys
input = sys.stdin.readline

def diffusion(grid):
    new_grid = [row[:] for row in grid]
    dusts = []
    for i in range(R):
        for j in range(C):
            if grid[i][j] != 0 and grid[i][j] != -1:
                dusts.append((i, j))
    
    dxs, dys = [0, 0, -1, 1], [-1, 1, 0, 0]
    for x, y in dusts:
        count = 0
        amount = grid[x][y] // 5
        for dx, dy in zip(dxs, dys):
            nx, ny = x+dx, y+dy
            if 0<= nx < R and 0<=ny<C and grid[nx][ny] != -1:
                new_grid[nx][ny] += amount
                count += 1
        new_grid[x][y] -= count*amount
        if new_grid[x][y] < 0: new_grid[x][y] = 0
    return new_grid

def clean(grid, cleaner):
    new_grid = [row[:] for row in grid]
    
    # 위쪽 공기청정기 (반시계 방향)
    up_row = cleaner[0]  # 위쪽 공기청정기 행

    # 1. 아래 경로:
    for j in range(1, C):
        new_grid[up_row][j] = grid[up_row][j-1]
    # 2. 오른쪽 경로:  (위로 이동)
    for i in range(up_row-1, -1, -1):
        new_grid[i][C-1] = grid[i+1][C-1]
    # 3. 위쪽 경로:
    for j in range(C-2, -1, -1):
        new_grid[0][j] = grid[0][j+1]
    # 4. 왼쪽 경로:
    for i in range(1, up_row):
        new_grid[i][0] = grid[i-1][0]
    # 공기청정기에서 나오는 바람은 깨끗 (0)
    new_grid[up_row][1] = 0
    
    # 아래쪽 공기청정기 (시계 방향)
    down_row = cleaner[1]  # 아래쪽 공기청정기 행
    #왼
    for i in range(R-2, down_row-1, -1):
        new_grid[i][0] = grid[i+1][0]
    #아래
    for j in range(C-2, -1, -1):
        new_grid[R-1][j] = grid[R-1][j+1]
    #오른
    for i in range(down_row+1, R):
        new_grid[i][C-1] = grid[i-1][C-1]
    #위
    for j in range(1, C):
        new_grid[down_row][j] = grid[down_row][j-1]
    # 공기청정기에서 나오는 바람은 깨끗 (0)
    new_grid[down_row][1] = 0
    
    new_grid[down_row][0] = -1
    new_grid[up_row][0] = -1
    return new_grid


R, C, T = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(R)]

cleaner = []
for i in range(R):
    if grid[i][0] == -1:
        cleaner.append(i)
cleaner = (cleaner[0], cleaner[1])  # (위쪽 행, 아래쪽 행)

for _ in range(T):
    grid = diffusion(grid)
    # print("after diff")
    # for g in grid:
    #     print(g)

    grid = clean(grid, cleaner)
    # print("after clean \n")
    # for g in grid:
    #     print(g)
total_dust = sum(sum(cell for cell in row if cell > 0) for row in grid)
print(total_dust)