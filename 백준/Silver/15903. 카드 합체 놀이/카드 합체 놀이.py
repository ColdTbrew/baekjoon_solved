n, m = map(int, input().split())
A = list(map(int, input().split()))

import heapq
heapq.heapify(A)

for _ in range(m):
    x = heapq.heappop(A)
    y = heapq.heappop(A)
    s = x + y
    heapq.heappush(A, s)
    heapq.heappush(A, s)

print(sum(A))