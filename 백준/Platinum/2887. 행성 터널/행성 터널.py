import sys

def find(parent, i):
    if parent[i] == i:
        return i
    parent[i] = find(parent, parent[i])
    return parent[i]

def union(parent, rank, i, j):
    root_i = find(parent, i)
    root_j = find(parent, j)

    if root_i != root_j:
        # rank숫자가 크면 더 낮은 트리 더 낮은 랭크의 트리를 높은 랭크의 트리 아래로 합친다
        if rank[root_i] < rank[root_j]:
            parent[root_i] = root_j
        elif rank[root_j] < rank[root_i]:
            parent[root_j] = root_i
        else:
            parent[root_j] = root_i
            rank[root_i] += 1
        return True
    return False # 이미 같은 집합

N = int(sys.stdin.readline())
planets = []
for i in range(N):
    x, y, z = map(int, sys.stdin.readline().split())
    planets.append((x,y ,z, i))

edges = []
planets.sort(key= lambda p:p[0])
for i in  range(N-1):
    cost = abs(planets[i][0] - planets[i+1][0])
    edges.append((cost, planets[i][3], planets[i+1][3])) # 엣지 인덱스 담기

planets.sort(key= lambda p:p[1])
for i in  range(N-1):
    cost = abs(planets[i][1] - planets[i+1][1])
    edges.append((cost, planets[i][3], planets[i+1][3])) # 엣지 인덱스 담기

planets.sort(key= lambda p:p[2])
for i in  range(N-1):
    cost = abs(planets[i][2] - planets[i+1][2])
    edges.append((cost, planets[i][3], planets[i+1][3])) # 엣지 인덱스 담기

edges.sort() # 비용순서로 소팅

parent = list(range(N)) # 각 원소의 부모를 저장하는 배열
rank = [0] * N # 트리의 높이를 저장하는 배열

min_total_cost = 0
num_edges_taken = 0

for cost, u, v in edges:
    if union(parent, rank, u, v): # 다른 그룹이면 합쳐서 T
        min_total_cost += cost
        num_edges_taken += 1
        if num_edges_taken == N-1: #N-1 개의 간선을 선택하면 MST 완성
            break
    
print(min_total_cost)


