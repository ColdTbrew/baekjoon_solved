import sys
input = sys.stdin.readline

R, C, M = map(int, input().split())

# 상어 정보 기록
grid = [[0 for _ in range(C)] for _ in range(R)]


# d = 1 위 2 아래 3 오른쪽 4왼쪽
for _ in range(M):
    r, c, s, d, z = map(int, input().split())
    grid[r-1][c-1] = [s, d, z]

# print(*grid, sep='\n')
direction = [(-1, 0), (1, 0), (0, 1), (0, -1)]
def move_and_eat():
    new_grid = [[0 for _ in range(C)] for _ in range(R)]

    for i in range(R):
        for j in range(C):
            if grid[i][j] != 0:# 상어가 있으면
                (s, d, z) = grid[i][j]
                dx, dy = direction[d-1]
                nx, ny = i, j
                if d == 1 or d == 2:
                    for _ in range(s):
                        if nx+dx<0 or nx+dx >=R: #넘어서면
                            dx = -dx
                        nx += dx
                else:
                    for _ in range(s):
                        if ny + dy <0 or ny + dy >= C:
                            dy = -dy
                        ny += dy
                if dx <0: new_d = 1
                elif dx > 0 : new_d = 2
                elif dy > 0 : new_d = 3
                else: new_d = 4

                if new_grid[nx][ny] == 0 or new_grid[nx][ny][2] < z:
                    new_grid[nx][ny] = [s, new_d, z]
    for i in range(R):
        for j in range(C):
            grid[i][j] = new_grid[i][j]

                        
ans = 0
for j in range(C): # 낚시왕의 위치
    #j 열의 있는 땅에 가장 가까운 상어 잡기
    for i in range(R):
        if grid[i][j] != 0:# 상어가 있으면 
            (s,d,z) = grid[i][j]#상어를 잡고 사라짐
            ans += z
            grid[i][j] = 0
            break
    #상어 이동
    move_and_eat()
    # print(*grid, sep='\n')
print(ans)