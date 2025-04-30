import sys
input = sys.stdin.readline
from collections import deque

N, M = map(int, input().split())
dependent = [[] for _ in range(N+1)]  # 후행 들을 기록
indegree = [0] * (N+1) # 차수를 기록
for _ in range(M):
    a, b= map(int, input().split())
    dependent[a].append(b)
    indegree[b] += 1

q = deque()
for i in range(1, N+1):
    if indegree[i] == 0:
        q.append(i)

ans = []
while q:
    cur = q.popleft()
    ans.append(cur)
    for next in dependent[cur]:
        indegree[next] -= 1
        if indegree[next] == 0:
            q.append(next)


print(*ans)