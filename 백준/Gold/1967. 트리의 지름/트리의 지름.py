import heapq
import sys
input = sys.stdin.readline

N = int(input().strip())

graph = [[] for _ in range(N+1)]

for _ in range(N-1):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))
    graph[v].append((u, w))

def dij(start):
    distances = [float('inf')] * (N+1)
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


result = dij(1) # 루트에서 다익스트라하고 루트에서 제일먼 노드 찾기
# print(result)
max_item = max(result[1:])
max_idx = result.index(max_item)
# print(max_item)
# print(max_idx)
result2 = dij(max_idx)
diameter = max(result2[1:])
print(diameter)
