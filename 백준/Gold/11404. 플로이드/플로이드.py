import sys
input = sys.stdin.readline

n = int(input().strip())
m = int(input().strip())

inf = float('inf')
dist = [[inf]* (n+1) for _ in range(n+1)]
for _ in range(m):
    a, b, c= map(int, input().split())
    dist[a][b] = min(dist[a][b], c)

for i in range(1, n+1):
    dist[i][i] = 0


# 플로이드 워셜
for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            # i - k , k - j 의 길이 유효할때
            if dist[i][k] != inf and dist[k][j] != inf:
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

for i in range(1, n+1):
    for j in range(1, n+1):
        print(dist[i][j] if dist[i][j] != inf else 0, end = " ")
    print()    

