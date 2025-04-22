import sys
input = sys.stdin.readline

N, E = map(int, input().split())
grid = [[] for _ in range(N+1)]
for i in range(E):
    a,b,c = map(int, input().split())
    grid[a].append((b, c))
    grid[b].append((a, c))

v1, v2 = map(int, input().split())
#1번 정점에서 N번 정점으로 이동할 때, 주어진 두 정점을 반드시 거치면서 최단 경로로 이동하는 프로그램을 작성하시오.
import heapq
def dij(start, end, grid, N):
    dist = [float('inf')] * (N+1)
    dist[start] = 0

    pq = [(0, start)]

    while pq:
        d, u = heapq.heappop(pq)
        if d > dist[u]:
            continue
        for v, w in grid[u]:
            if dist[v] > dist[u] + w:
                dist[v] = dist[u] + w
                heapq.heappush(pq, (dist[v] , v))
    return dist[end]

path1 = dij(1, v1, grid, N) + dij(v1, v2, grid, N) + dij(v2, N, grid, N)
path2 = dij(1, v2, grid, N) + dij(v2, v1, grid, N) + dij(v1, N, grid, N)
print(min(path1, path2)if min(path1, path2) != float('inf') else -1)