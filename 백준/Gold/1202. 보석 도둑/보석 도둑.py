import sys
input = sys.stdin.readline

N, K = map(int, input().split())
# 그리디, 우선순위 큐로 구현해야함
# 그 순간에 할 수 있는 최고의 선택을해야함
# value를 내림차순 무게를 오름차순
jewels = []
import heapq
for _ in range(N):
    w, v = map(int, input().split())
    jewels.append((w, v))


bags = []
for _ in range(K):
    w = int(input())
    bags.append(w)

jewels.sort(key = lambda x : (x[0], -x[1])) # 가격 내림차순, 무게 오름차순
bags.sort() # 오름차순

total_value = 0
jewel_idx =0

pq = []
# print("jewels", jewels)
# print("bags", bags)
for bag in bags:
    # print("bag", bag)
    # print("jewels[jewel_idx][0]", jewels[jewel_idx][0])
    while jewel_idx < N and jewels[jewel_idx][0] <= bag: # 무게가 작은 백보다 작을때까지
        heapq.heappush(pq, -jewels[jewel_idx][1]) #밸류 맥스힙
        jewel_idx += 1
    # print("pq", pq)
    if pq:
        total_value += -heapq.heappop(pq)
print(total_value)