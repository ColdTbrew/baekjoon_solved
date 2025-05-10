import sys
input = sys.stdin.readline
# sys.setrecursionlimit(10**6)

N, M = map(int, input().split())
# N개의 점
# M개의 간선
parent = [i for i in range(N)]
def find(x):
    while parent[x] != x:
        parent[x] = parent[parent[x]]  # 경로 압축
        x = parent[x]
    return x
def union(x, y):
    x = find(x)
    y = find(y)
    if x != y:
        parent[y] = x

cycle_found = False

for count in range(1, M+1):
    u, v = map(int, input().split())
    if find(u) == find(v):
        # 같은 집합이면 사이클 발생 = 부모가 같으면
        print(count)
        cycle_found = True
        break
    else:
        union(u, v)

if not cycle_found:
    print(0)
# 사이클이 존재하는지 알려면 dfs를 사용해서 visited 배열을 활용해 visited한 노드인데 부모가 아니라면 사이클이 존재함을 알 수 있음


