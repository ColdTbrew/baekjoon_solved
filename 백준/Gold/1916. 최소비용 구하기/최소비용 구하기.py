import sys
input = sys.stdin.readline

N = int(input().strip())
M = int(input().strip())

graph = [[] for _ in range(N+1)]

for _ in range(M):
    u, v, cost = map(int, input().split())
    graph[u].append((v, cost))

# print(graph)

import heapq
def dij(start):
    dists = [float('inf') for _ in range(N+1)]
    pq = []
    pq.append((0, start))
    dists[start] = 0

    while pq:
        (dist, cur) = heapq.heappop(pq)
        if dists[cur] < dist:
             continue
        for next_node, cost in graph[cur]:
            new_dist = dist+cost
            if dists[next_node] > new_dist:
                dists[next_node] = new_dist
                heapq.heappush(pq, (new_dist, next_node))
    return dists
    
start, end = map(int, input().split())
print(dij(start)[end])