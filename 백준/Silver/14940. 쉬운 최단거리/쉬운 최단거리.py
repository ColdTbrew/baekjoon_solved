import sys
from collections import deque

input = sys.stdin.readline

# 입력
n, m = map(int, input().split())
graph = []
target = None  # 목표 지점 좌표

for i in range(n):
    row = list(map(int, input().split()))
    graph.append(row)
    # 목표 지점 찾기
    for j in range(m):
        if row[j] == 2:
            target = (i, j)

# 거리 배열 초기화
dist = [[-1] * m for _ in range(n)]
for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            dist[i][j] = 0  # 갈 수 없는 땅은 0

# BFS
dxs, dys = [0, 0, -1, 1], [1, -1, 0, 0]  # 동서남북
q = deque([target])
dist[target[0]][target[1]] = 0  # 목표 지점 거리 0

while q:
    x, y = q.popleft()
    for dx, dy in zip(dxs, dys):
        nx, ny = x + dx, y + dy
        if 0 <= nx < n and 0 <= ny < m and dist[nx][ny] == -1 and graph[nx][ny] != 0:
            dist[nx][ny] = dist[x][y] + 1
            q.append((nx, ny))

# 출력
for row in dist:
    print(*row)