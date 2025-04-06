from collections import deque
import sys
input = sys.stdin.readline

#cut_line 이 min 부터 max까지

N = int(input().strip())
min_h, max_h = float('inf'), 0

graph = [[] for _ in range(N)]



for i in range(N):
    row = list(map(int, input().split()))
    graph[i] = row
    for r in row:
        if r > max_h:
            max_h = r
        if r < min_h:
            min_h = r
            
max_area = 0


def bfs(i, j, height):
    q = deque()
    q.append((i, j))
    visited = [[False for _ in range(N)] for _ in range(N)]
    visited[i][j] = True
    dxs, dys = [0, 0, -1, 1], [1, -1, 0, 0]

    while q:
        i, j = q.popleft()
        for dx, dy in zip(dxs, dys):
            nx = dx+i
            ny = dy+j
            if 0<=nx < N and 0<=ny<N and not visited[nx][ny] and graph[nx][ny]>height:
                visited[nx][ny] = True
                q.append((nx, ny))
                global_visited[nx][ny] = True


for cut_line in range(0, max_h):
    # bfs를 돌릴거임
    area_count = 0
    global_visited = [[False for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):            
            if graph[i][j] > cut_line and not global_visited[i][j]:
                # print("start bfs")
                area_count += 1
                bfs(i, j, cut_line)
    # print(area_count)
    max_area = max(area_count, max_area)

print(max_area)