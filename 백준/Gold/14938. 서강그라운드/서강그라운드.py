import sys
input = sys.stdin.readline

N, M, R = map(int, input().split())
items = list(map(int, input().split()))

graph = [[] for _ in range(N)]
for _ in range(R):
    a, b, lenght = map(int, input().split())
    graph[a - 1].append((b - 1, lenght))
    graph[b - 1].append((a - 1, lenght))

from collections import deque
# print(graph)
def bfs(start):
    max_item = 0
    q = deque()
    q.append((start, 0))
    distances = [float('inf')] * N
    distances[start] = 0
    while q:
        cur, dist = q.popleft()
        for neighboor, lenght in graph[cur]:
            new_dist = dist+lenght
            if new_dist <= M and new_dist < distances[neighboor]:
                distances[neighboor] = new_dist
                q.append((neighboor, new_dist))
    for i in range(N):
        if distances[i] <= M:
            max_item += items[i]

    return max_item


max_count = 0
for i in range(N):
    # i 번에 떨어진다
    max_count = max(max_count, bfs(i))
    # print(i, bfs(i))
print(max_count)