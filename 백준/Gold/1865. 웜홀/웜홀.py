
from sys import stdin
input = stdin.readline

def bf():
    for i in range(n):
        for cur, next, cost in edges:
            if dist[next] > dist[cur] + cost:
                dist[next] = dist[cur] + cost
                if i == n - 1:
                    return True
    return False
                        
TC = int(input())

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
    dist = [1e9] * (n+1)
    if bf():
        print("YES")
    else:
        print("NO")