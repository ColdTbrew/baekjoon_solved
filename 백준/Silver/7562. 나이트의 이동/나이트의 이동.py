N = int(input())

from collections import deque
def bfs(size, si, sj, ei, ej):
    if si == ei and sj == ej:
        return 0
    visited = [[-1] * size for _ in range(size)]
    q = deque()
    q.append((si, sj))
    visited[si][sj] = 0
    dxs = [1, 2, 2, 1, -1, -2, -2, -1]
    dys = [2, 1, -1, -2, -2, -1, 1, 2]
    

    while q:
        curi, curj = q.popleft()
        if  curi == ei and curj == ej:
            return visited[curi][curj]
        for dx, dy in zip(dxs, dys):
            nx, ny = curi+dx, curj + dy
            if 0<=nx<size and 0<=ny<size and visited[nx][ny] == -1:
                visited[nx][ny] = visited[curi][curj] + 1
                q.append((nx,ny))
    return -1    

for _ in range(N):
    size = int(input())
    si, sj = map(int, input().split())
    ei, ej = map(int, input().split()) 
    print(bfs(size, si,sj,ei,ej))