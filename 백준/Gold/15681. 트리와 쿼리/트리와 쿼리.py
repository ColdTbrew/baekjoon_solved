import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

N, R, Q = map(int, input().split())
connect = [[] for _ in range(N+1)]
for _ in range(N-1):
    u, v = map(int, input().split())
    connect[v].append(u)
    connect[u].append(v)

subtree_size = [0] * (N+1)
visited = [False] *(N+1)

def dfs(now):
    visited[now] = True
    subtree_size[now] = 1
    for next_node in connect[now]:
        if not visited[next_node]:
            subtree_size[now] += dfs(next_node)
    return subtree_size[now]

dfs(R)

for _ in range(Q):
    u = int(input())
    print(subtree_size[u])
