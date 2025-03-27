V, E = map(int, input().split())
K = int(input())
graph = [[] for _ in range(V+1)]

import heapq
import sys
input = sys.stdin.readline

for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))

def dij(start):
    distances = [float('inf')] * (V+1)
    distances[start] = 0
    pq = [(0, start)]
    while pq:
        dist, cur = heapq.heappop(pq)
        if dist > distances[cur]: # 이미 최단거리면
            continue
        for (next_node, weight) in graph[cur]:
            new_dist = dist + weight
            # 더 짧으면 갱신
            if new_dist < distances[next_node]:
                distances[next_node] = new_dist
                heapq.heappush(pq, (new_dist, next_node))
    return distances


result = dij(K)
for i in range(1, V+1):
    print(result[i] if result[i] != float('inf') else "INF")