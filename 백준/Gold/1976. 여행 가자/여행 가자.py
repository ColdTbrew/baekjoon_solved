
N = int(input())
M = int(input())

graph = [list(map(int,input().split())) for _ in range(N)]
target = list(map(int, input().split()))
def union(a, b):
    a_p = find(a)
    b_p = find(b)
    if a_p < b_p:
        parent[b_p] = a_p
    else:
        parent[a_p] = b_p

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

parent = [x for x in range(N)] # 자기 자신이 루트인걸로 다 만들어줌

for a in range(N):
    for b in range(N):
        if graph[a][b] == 1:
            union(a, b)
ans = "YES"
first_city_root = find(target[0] - 1)
for t in target:
    if find(t-1) != first_city_root:
        ans = "NO"
        break
print(ans)