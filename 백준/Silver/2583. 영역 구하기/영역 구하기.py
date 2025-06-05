import sys
input = sys.stdin.readline

N, M, K = map(int, input().split())
grid = [[0] * N for _ in range(M)]

# print(*grid, sep='\n')
for _ in range(K):
    x1, y1, x2, y2 = map(int, input().split())
    for x in range(x1, x2):
        for y in range(y1, y2):
            # print(x, y)
            grid[x][y] = 1

# print(*grid, sep='\n')

from collections import deque
visited = [[False] * N for _ in range(M)]
def bfs(i, j):
    q = deque()
    q.append((i, j))
    
    visited[i][j] = True

    dxs, dys = [0, 0, -1, 1], [-1, 1, 0, 0]
    count = 1
    while q:
        curi, curj = q.popleft()
        for dx, dy in zip(dxs, dys):
            nx, ny = dx+curi, dy+curj
            if 0<=nx<M and 0<=ny<N and not visited[nx][ny] and grid[nx][ny] == 0:
                count += 1
                q.append((nx, ny))
                visited[nx][ny] = True

    return count
counts = []
for i in range(M):
    for j in range(N):
        if grid[i][j] == 0 and not visited[i][j]:
            c = bfs(i, j)
            counts.append(c)

print(len(counts))
counts.sort()
print(*counts)