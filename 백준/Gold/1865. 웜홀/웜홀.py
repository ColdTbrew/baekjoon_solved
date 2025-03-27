import sys
input = sys.stdin.readline

TC = int(input().strip())
for _ in range(TC):
    n, m, w = map(int, input().split())

    edges = []

    for _ in range(m):
        s, e, t = map(int, input().split())
        edges.append((s, e, t))
        edges.append((e, s, t))
    for _ in range(w):
        s, e, t = map(int, input().split())
        edges.append((s, e, -t))
    
    def bellman_ford():
        dists = [1e9] * (n+1)

        for _ in range(n-1): # 벨만 포드 알고리즘은 n-1 번만 완화를 수행해도 최단거리가 다 구해짐
            for s, e, t in edges:
                if dists[s] + t < dists[e]:
                    dists[e] = dists[s] + t

            
        for s, e, t in edges: # 하지만 한번 더 돌렸을때 갱신이 된다면 음수의 사이클이 존재한다는 의미
            if dists[s] + t < dists[e]:
                return True
        return False
    
    if bellman_ford():
        print("YES")
    else:
        print("NO")