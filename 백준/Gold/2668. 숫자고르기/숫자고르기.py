import sys
import heapq
input = sys.stdin.readline


N = int(input())
graph = [[] for _ in range(N+1)]
for i in range(N):
    graph[int(input())].append(i+1)

# print(graph)

def dfs(u, visited):
    visited.add(u)
    checked[u] = 1
    for v in graph[u]: # 이웃탐색하면서
        if v not in visited: # 방문기록에 없으면
            dfs(v, visited.copy()) # 재귀
        else:
            result.extend(list(visited)) # 방문 기록있으면 사이클이니까 정답에 포함
            return
        
checked = [0 for _ in range(N+1)]
result = []
for i in range(1, N+1):
    if not checked[i]:
        dfs(i, set([]))

result.sort()
print(len(result))
print(*result, sep = '\n')