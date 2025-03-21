import sys
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]

for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

visited = [False for _ in range(N+1)]
count = 0
from collections import deque
for node in range(1, N+1):
    if not visited[node]:
        count += 1
        q = deque()
        q.append(node)
        visited[node] = True
        while q:
            neigh = q.popleft()
            for new in graph[neigh]:
                if not visited[new]:
                    q.append(new)
                    visited[new] = True

print(count)