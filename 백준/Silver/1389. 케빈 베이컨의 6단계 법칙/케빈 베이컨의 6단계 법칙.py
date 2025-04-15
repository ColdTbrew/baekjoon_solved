from collections import Counter
import sys
input = sys.stdin.readline

# 케빈 베이컨의 수는 나를 제외한 다른 사람까지의 dist의 총합이라고 볼 수 있다.
N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split()) 
    graph[a].append((b, 1))
    graph[b].append((a, 1))

import heapq
#각 위치에서 다익스트라 실행해서 길이 셈
def dij(start):
    distances = [float('inf')] * (N+1)
    pq = [(0, start)]
    distances[start] = 0
    while pq:
        cur_dist,cur_node = heapq.heappop(pq)
        if cur_dist > distances[cur_node]:
            continue
        for next_node, weight in graph[cur_node]:
            distance = cur_dist + weight
            if distance < distances[next_node]:
                distances[next_node] = distance
                heapq.heappush(pq, (distance, next_node))
    total_dist = sum(d for d in distances[1:N+1] if d != float('inf') and d != 0)
    return total_dist

min_bacon = float('inf')
min_person = N+1
for i in range(1,N+1):
    bacon = dij(i)
    if bacon < min_bacon or (bacon == min_bacon and i < min_person):
        min_bacon = bacon
        min_person = i
print(min_person)
