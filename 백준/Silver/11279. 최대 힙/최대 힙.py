import sys
input = sys.stdin.readline

N = int(input().strip())

import heapq

pq = []
for _ in range(N):
    x = int(input().strip())
    if x == 0:
        if pq:
            print(-heapq.heappop(pq))
        else:
            print(0)
    else:
        heapq.heappush(pq, -x)