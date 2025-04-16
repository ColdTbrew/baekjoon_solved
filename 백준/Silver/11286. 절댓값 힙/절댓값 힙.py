import sys
input = sys.stdin.readline

T = int(input())
import heapq
pq = []
for _ in range(T):
    cmd = int(input())
    if cmd != 0:
        heapq.heappush(pq, (abs(cmd), cmd))
    else:
        if pq:
            print(heapq.heappop(pq)[1])
        else:
            print(0)
