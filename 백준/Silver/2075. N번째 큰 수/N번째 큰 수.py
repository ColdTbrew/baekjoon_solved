import sys
import heapq
input = sys.stdin.readline

N = int(input())

pq = []
for i in range(N):
    row = list(map(int, input().split()))
    for x in row:
        if len(pq) < N:
            heapq.heappush(pq, x)
        else:
            if pq[0] < x: # 나보다 작은 값이 있으면 제거후 넣기
                heapq.heappop(pq)
                heapq.heappush(pq, x)

print(pq[0])
