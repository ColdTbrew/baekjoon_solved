N, K = map(int, input().split())
from collections import deque

def bfs(N, K):
    if N >= K:  # N이 K보다 크거나 같으면 뒤로만 가는 게 최적
        return N - K
    q = deque()
    q.append(N)
    visited = [-1] * (100001)
    visited[N] = 0
    while q:
        cur = q.popleft()
        if cur == K:
            return visited[cur]
        if cur * 2<= 100000 and visited[cur*2] == -1:
            visited[cur*2] = visited[cur]
            q.appendleft(cur*2)
        if cur - 1 >= 0 and visited[cur-1] == -1:
            visited[cur-1] = visited[cur] + 1
            q.append(cur-1)
        if cur + 1 <= 100000 and visited[cur+1] == -1:
            visited[cur+1] = visited[cur] + 1
            q.append(cur+1)

print(bfs(N, K))
