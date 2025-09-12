N, M = map(int, input().split())

graph = [[] for _ in range(N+1)]
for _ in range(M):
    a,b,c = map(int, input().split())
    graph[a].append((b, c))
# c는 음수가능 -> 다익스트라 못씀 -> 벨만 포드 알고리즘

dist = [float('inf')] * (N+1)
dist[1] = 0
for i in range(N): # N번 반복하는데
    for idx, temp in enumerate(graph):
        if idx == 0: # 1에서 시작해서 뺌
            continue
        for to_node, cost in temp:
            #현재 까지 to_node까지의 비용보다 지금 노드를 거쳐 가는 편이 저렴할 때
            if dist[idx] != float('inf') and dist[idx] + cost < dist[to_node]:
                dist[to_node] = dist[idx] + cost
                if i == N-1:
                    print(-1)
                    exit()
for i in range(2, N+1):
    if dist[i] == float('inf'):
        print(-1)
    else:
        print(dist[i])

