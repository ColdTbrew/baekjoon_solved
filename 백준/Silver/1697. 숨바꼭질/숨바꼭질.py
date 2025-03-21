import sys
input = sys.stdin.readline

N, K = map(int, input().split())

visited = [False] * 100001

from collections import deque
q = deque()
q.append((N, 0))
visited[N] = True
while q:
    now, time = q.popleft()
    if now == K:
        print(time)
        break
    for i in range(3):
        if i == 0:
            new = now - 1
        elif i == 1:
            new = now + 1
        else:
            new = now*2
        if 0<=new<len(visited) and not visited[new]:
            q.append((new, time+1))
            visited[new] = True
            
