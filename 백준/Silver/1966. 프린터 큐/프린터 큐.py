import sys
input = sys.stdin.readline

T = int(input())
import heapq
from collections import deque
for _ in range(T):
    N, M = map(int, input().split())
    priority = list(map(int, input().split()))
    queue = deque([(p, i) for i, p in enumerate(priority)])
    max_heap = [-p for p in priority]
    heapq.heapify(max_heap)

    print_order = 0

    while queue:
        priority, index = queue.popleft()
        if -max_heap[0] == priority:
            print_order += 1
            heapq.heappop(max_heap)
            if index == M:
                print(print_order)
                break
        else:
            queue.append((priority, index))