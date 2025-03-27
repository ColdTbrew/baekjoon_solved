import sys
input = sys.stdin.readline

n, m, x = map(int, input().split())

inf = float('inf')
graph = [[] for _ in range(n+1)]

for _ in range(m):
    u, v, t = map(int, input().split())
    graph[u].append((v,t))

import heapq

def dij(start):
    pq = [(start, 0)]
    dists = [inf for _ in range(n+1)]
    dists[start] = 0

    while pq:
        cur, dist = heapq.heappop(pq)
        if dist > dists[cur]:
            continue
        for n_node, w in graph[cur]:
            new_dist = dist+w
            if new_dist < dists[n_node]:
                dists[n_node] = new_dist
                heapq.heappush(pq, (n_node, new_dist))

    return dists

x_to_all = dij(x)
# print(x_to_all)

ans = 0
for i in range(1, n+1):
    if i != x:
        result = dij(i)
        add_time = x_to_all[i] + result[x]
        # print(add_time)
        # print(result)
        ans = max(ans, add_time)

print(ans)