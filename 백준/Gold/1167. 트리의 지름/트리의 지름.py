import sys
input = sys.stdin.readline

N = (int(input()))
graph = [[] for _ in range(N+1)]

for _ in range(1, N+1):
    row = list(map(int, input().split()))
    v = row[0]
    for i in range(1, len(row)-1, 2):
        u, w = row[i], row[i+1]
        graph[v].append((u, w))
        graph[u].append((v, w))
from collections import deque
def bfs(start):
    dist = [-1] * (N+1)
    dist[start] = 0
    q = deque([start])
    max_dist, max_node = 0, start

    while q:
        v = q.popleft()
        for u, w in graph[v]:
            if dist[u] == -1:
                dist[u] = dist[v] + w
                q.append(u)
                if dist[u] > max_dist:
                    max_dist = dist[u]
                    max_node = u
    return max_node, max_dist

farthest_node, _ = bfs(1)
_ , diameter = bfs(farthest_node)
print(diameter)