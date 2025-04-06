import sys

N = int(input())

grid = [list(map(int, input())) for _ in range(N)]

dxs, dys = [0, 0, -1, 1], [1, -1, 0, 0]
from collections import deque
def bfs(i, j):
    visit = [[False] * N for _ in range(N)]
    q = deque([(i, j)])
    visit[i][j] = True
    count = 1
    while q:
        i, j = q.popleft()
        for dx, dy in zip(dxs, dys):
            nx = dx + i
            ny = dy + j
            if 0 <= nx < N and 0<=ny<N and not visit[nx][ny] and grid[nx][ny] == 1:
                visit[nx][ny] = True
                global_visit[nx][ny] = True
                q.append((nx, ny))
                count += 1
    return count

danji = 0
global_visit = [[False] * N for _ in range(N)]
house_count = []
for i in range(N):
    for j in range(N):
        if grid[i][j] == 1 and not global_visit[i][j]: 
            danji += 1
            house_count.append(bfs(i, j))

print(danji)
print(*sorted(house_count), sep = "\n")