import sys 
input = sys.stdin.readline

V, E = map(int, input().split())
tree = [[] for _ in range(V+1)]
for _ in range(E):
    a, b, c = map(int, input().split())
    tree[a].append((b, c))
    tree[b].append((a, c))
import heapq
def prim(start):
    weight = 0
    visited = set()
    pq = [(0, start)] #가중치, 노드
    while pq and len(visited) < V:
        dist, node = heapq.heappop(pq)

        if node in visited:
            continue

        visited.add(node)
        weight += dist

        for next_node, next_dist in tree[node]:
            if next_node not in visited:
                heapq.heappush(pq, (next_dist, next_node))

    return weight if len(visited) == V else float('inf')
    
print(prim(1))