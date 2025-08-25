import sys
import heapq

dxs, dys = [0, 0, -1, 1], [-1,1,0,0]
def dij(N, startx, starty, graph):
    cost = 0
    pq = []
    heapq.heappush(pq, [graph[0][0], startx, starty])
    dist = [[float('inf') for _ in range(N)] for _ in range(N)]
    dist[0][0] =  graph[0][0]
    # print(dist)
    while pq:
        cur_cost, x, y = heapq.heappop(pq)
        if dist[x][y] < cur_cost: # 이미 적혀있는게 더 작다면
            continue
        for dx, dy in zip(dxs, dys):
            nx, ny = x+dx, y+dy
            if 0<= nx < N and 0<=ny < N:
                temp = cur_cost + graph[nx][ny]
                if temp < dist[nx][ny]:
                    dist[nx][ny] = temp
                    heapq.heappush(pq, [temp, nx, ny])
    return dist[N-1][N-1]                
    
num = 1
while 1:
    N = int(input())
    if N == 0:
        break
    graph = []
    for _ in range(N):
        graph.append(list(map(int, input().split())))
    print(f"Problem {num}:", end =" ")
    print(dij(N, 0, 0, graph))
    num += 1
