import sys
input = sys.stdin.readline

N, M, V = map(int, input().split())

graph = [[] for _ in range(N+1)]
for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

# print(graph)
from collections import deque
def bfs(start):
    visited_order = []
    q = deque([start])
    visited = [False] * (N+1)
    visited[start] = True
    visited_order.append(start)

    while q:
        cur_node = q.popleft()
        for neighbor in sorted(graph[cur_node]):
            if not visited[neighbor]:
                visited[neighbor] = True
                q.append(neighbor)
                visited_order.append(neighbor)
    return visited_order
def dfs_func(start):
    visited = [False] * (N+1)
    visited_order = [start]
    visited[start] = True
    def dfs(node):
        if not graph[node]:
            # print("return")
            return
        for neighbor in sorted(graph[node]):
            # print("ne : ", neighbor)
            if not visited[neighbor]:
                visited[neighbor] = True
                visited_order.append(neighbor)
                dfs(neighbor)

    dfs(start)
    return visited_order    

dfs_order = dfs_func(V)
print(*dfs_order)

bfs_order = bfs(V)
print(*bfs_order)
