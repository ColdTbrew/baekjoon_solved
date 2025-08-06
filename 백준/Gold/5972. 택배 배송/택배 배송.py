import sys
import heapq
input = sys.stdin.readline

N, M = map(int, input().split())
#다익스트라 
# a - > b로 가는 경로의 cost를 적어두고 최단경로 갱신

graph = [[] for _ in range(N+1)]
for _ in range(M):
    u, v, cost = map(int, input().split())
    graph[u].append((v, cost))
    graph[v].append((u, cost))

distances = [float('inf')] * (N+1)

def dij(start):
    q = []
    distances[start] = 0
    heapq.heappush(q, (0, start)) 
    while q:
        dist, now = heapq.heappop(q)
        if distances[now] < dist: # 이미 최단거리이면
            continue
        for i in graph[now]: # 최단 거리가 있는지 탐색
            if dist + i[1] < distances[i[0]]:
                distances[i[0]] = dist + i[1]
                heapq.heappush(q, (dist+i[1], i[0]))
                
dij(1)
# print(graph)
print(distances[N])