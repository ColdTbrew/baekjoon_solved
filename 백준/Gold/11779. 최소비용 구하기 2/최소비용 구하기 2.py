import sys
input = sys.stdin.readline
from collections import deque

N = int(input())
M = int(input())
graph = [[] for _ in range(N+1)]
for i in range(M):
    depart, dest, cost = map(int, input().split())
    graph[depart].append((dest, cost))

start, end = map(int, input().split())
import heapq
def dij(start, end):
    distances = [float('inf')] * (N+1)
    q = []
    prev_paths = [-1 for _ in range(N+1)]
    heapq.heappush(q, (0, start))
    distances[start] = 0
    
    while q:
        dist, cur = heapq.heappop(q)
        if distances[cur] < dist:
            continue
        for next_node, cost in graph[cur]:
            new_cost = dist + cost
            if new_cost < distances[next_node]:
                distances[next_node] = new_cost
                prev_paths[next_node] = (cur)
                heapq.heappush(q, (new_cost, next_node))
    path = []
    current = end
    while current != -1:
        path.append(current)
        current = prev_paths[current]
    path.reverse()
    return distances, path

dist, paths = dij(start, end)
print(dist[end])
print(len(paths))
print(*paths)