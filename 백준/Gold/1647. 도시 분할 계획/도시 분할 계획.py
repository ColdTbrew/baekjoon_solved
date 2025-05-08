import sys
input = sys.stdin.readline

N, M = map(int, input().split())
roads = []

# idea : mst를 만들거임 union,find 이용해서

for _ in range(M):
    a, b, c = map(int, input().split())
    roads.append((c, a, b))

# 최소 비용 정렬
roads.sort()

#자기 자신이 부모라고 일단 정의
parent = [i for i in range(N+1)]

def find(x): # 부모를 찾는 함수
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    # 부모가 다르면 부모를 바꿈
    x_root = find(x)
    y_root = find(y)
    if x_root != y_root:
        if x_root < y_root: #숫자가 작은 루트가 부모가됨
            parent[y_root] = x_root
        else:
            parent[x_root] = y_root

total_cost = 0
max_edge_cost = 0

for cost, a, b in roads: #작은 코스트인 길부터 불러와서 점점합침 -> mst의 코스트 계산
    if find(a)!= find(b):
        union(a, b)
        total_cost += cost
        max_edge_cost = max(max_edge_cost, cost)


print(total_cost-max_edge_cost)