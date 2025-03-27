import sys
input = sys.stdin.readline

TC = int(input())
for _ in range(TC):
    n, m, w = map(int, input().split())
    edges = []

    # 도로 (양방향)
    for _ in range(m):
        s, e, t = map(int, input().split())
        edges.append((s, e, t))
        edges.append((e, s, t))
    # 웜홀 (단방향, 음수)
    for _ in range(w):
        s, e, t = map(int, input().split())
        edges.append((s, e, -t))
    
    def bellman_ford():
        dists = [0] * (n + 1)  # 모든 정점을 0으로 초기화
        
        for i in range(n):
            for s, e, t in edges:
                if dists[e] > dists[s] + t:
                    dists[e] = dists[s] + t
                    if i == n - 1:  # N번째 갱신
                        return True
        return False
    
    if bellman_ford():
        print("YES")
    else:
        print("NO")