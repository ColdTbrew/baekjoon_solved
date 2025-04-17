import sys
from collections import deque

input = sys.stdin.readline

N = int(input().strip())
color = [list(input().strip()) for _ in range(N)]

def bfs(i, j):
    q = deque([(i, j)])
    visited[i][j] = True
    dxs, dys = [0, 0, -1, 1], [-1,1,0,0]
    cur_color = color[i][j]
    while q:
        x, y = q.popleft()
        for dx, dy in zip(dxs, dys):
            nx, ny = x+dx , y+dy
            if 0<=nx<N and 0<=ny<N and color[nx][ny] == cur_color and not visited[nx][ny]:
                visited[nx][ny] = True
                q.append((nx, ny))

def blind_bfs(i, j):
    q = deque([(i, j)])
    blind_visited[i][j] = True
    dxs, dys = [0, 0, -1, 1], [-1,1,0,0]
    cur_color = color[i][j]
    is_same_color = ['B']
    if cur_color == 'R' or cur_color == 'G':
        is_same_color = ['R', 'G']
    while q:
        x, y = q.popleft()
        for dx, dy in zip(dxs, dys):
            nx, ny = x+dx , y+dy
            if 0<=nx<N and 0<=ny<N and color[nx][ny] in is_same_color and not blind_visited[nx][ny]:
                blind_visited[nx][ny] = True
                q.append((nx, ny))

visited = [[False] * N for _ in range(N)]
blind_visited = [[False] * N for _ in range(N)]
count = 0
blind_count = 0
for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            bfs(i, j)
            count += 1        
        if not blind_visited[i][j]:
            blind_bfs(i,j)
            blind_count += 1
print(count, blind_count)