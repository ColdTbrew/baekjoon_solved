N = int(input())
lectures = [list(map(int,input().split())) for _ in range(N)]
# print(lectures)
lectures.sort(key = lambda x : x[0])

import heapq

rooms = []
heapq.heappush(rooms, lectures[0][1])

for start, end in lectures[1:]:
    if start >= rooms[0]: #강의실 재사용
        heapq.heappop(rooms)
        heapq.heappush(rooms, end)
    else:
        heapq.heappush(rooms, end)


    
print(len(rooms))
