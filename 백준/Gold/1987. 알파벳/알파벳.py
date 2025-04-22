import sys
input = sys.stdin.readline

R, C = map(int, input().split())
grid = [[] for _ in range(R)]
for i in range(R):
    row = list(input().strip())
    grid[i] = row
# print(grid)
starti, startj = 0, 0
from collections import deque
dxs, dys = [0, 0, -1, 1],[-1,1, 0, 0]
def dfs(i, j, used_alpha):
    global max_lenght
    max_lenght = max(max_lenght, len(used_alpha))

    for dx, dy in zip(dxs, dys):
        nx , ny= i+dx, j+dy
        if 0<=nx <R and 0<= ny < C and grid[nx][ny] not in used_alpha:
            used_alpha.add(grid[nx][ny])
            dfs(nx, ny, used_alpha)
            used_alpha.remove(grid[nx][ny])
max_lenght = 1
used_alpha = set(grid[starti][startj])
dfs(starti, startj, used_alpha)

print(max_lenght)
