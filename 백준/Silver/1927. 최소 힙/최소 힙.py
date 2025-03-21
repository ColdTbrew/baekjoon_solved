import sys
input = sys.stdin.readline

T = int(input().strip())
import heapq
heap = []
heapq.heapify(heap)
for _ in range(T):
    x = int(input().strip())
    if x == 0:
        if not heap:
            print(0)
        else:
            print(heapq.heappop(heap))
    else:
        heapq.heappush(heap, x)
