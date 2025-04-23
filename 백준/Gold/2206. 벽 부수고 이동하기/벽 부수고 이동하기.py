import sys
input = sys.stdin.readline

N,M = map(int, input().split())
graph = [list(map(int, input().rstrip())) for _ in range(N)]

from collections import deque
def dij(starti, startj, endi, endj):
    dist = [[[float('inf')]*2 for _ in range(M)] for _ in range(N)] 
    q = deque()
    q.append((starti, startj, 0))
    dist[starti][startj][0] = 1
    dxs, dys = [0, 0, -1, 1], [-1, 1, 0, 0]

    while q:
        curi, curj, broken = q.popleft()
        if curi == endi and curj == endj:
            return dist[endi][endj][broken]
        for dx, dy in zip(dxs, dys):
            nx, ny = curi + dx, curj+dy
            
            if 0<=nx<N and 0<=ny < M:
                if graph[nx][ny] == 0 and dist[nx][ny][broken] == float('inf'):
                    dist[nx][ny][broken] = dist[curi][curj][broken] +1
                    q.append((nx, ny, broken))
                elif graph[nx][ny] == 1 and broken==0 and dist[nx][ny][1] == float('inf'):
                    dist[nx][ny][1] = dist[curi][curj][broken] +1
                    q.append((nx, ny, 1))
    return float('inf')
min_dist = dij(0, 0, N-1, M-1)

print(min_dist if min_dist != float('inf') else -1)

