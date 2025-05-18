import sys
input = sys.stdin.readline
from collections import deque
import heapq

N, M = map(int, input().split())

#차수를 저장하는 n개
indegree = [0] * (N+1)
# 우선순위들
dependent = [[] for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, input().split())
    dependent[a].append(b) #a뒤에 b를 풀어라
    indegree[b] += 1

pq = []
# indegree가 0인거부터 넣자 + 숫자가 작은거부터
for i in range(1, N+1):
    if indegree[i] == 0:
        heapq.heappush(pq, i)

ans = []
while pq:
    cur = heapq.heappop(pq)
    ans.append(cur)
    for next in dependent[cur]:
        indegree[next] -= 1
        if indegree[next] == 0:
            heapq.heappush(pq, next)
print(*ans)