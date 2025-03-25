import sys
from collections import deque
input = sys.stdin.readline

N = int(input().strip())

graph = [[] for _ in range(N+1)]
parent = [0 for _ in range(N+1)]

for _ in range(N-1):
    u, v = map(int, input().strip().split())
    graph[u].append(v)
    graph[v].append(u)

# BFS로 부모 찾기
def bfs(start):
    queue = deque([start])
    parent[start] = -1  # 루트
    while queue:
        node = queue.popleft()
        for next_node in graph[node]:
            if parent[next_node] == 0:  # 방문하지 않은 경우
                parent[next_node] = node
                queue.append(next_node)

bfs(1)

for i in range(2, N+1):
    print(parent[i])