from collections import deque
import sys
input = sys.stdin.readline


N, M = map(int, input().split())

graph = [[] for _ in range(N)]
for i in range(N):
    row = list(map(int, input().split()))
    graph[i] = row
    



def bfs(i, j, global_visited):
    q = deque()
    q.append((i, j))
    global_visited[i][j] = True
    dxs, dys = [0, 0, -1, 1], [1, -1, 0, 0]
    
    
    while q:
        i, j = q.popleft()
        for dx, dy in zip(dxs, dys):
            nx = dx+i
            ny = dy+j
            if 0<=nx < N and 0<=ny<M and not global_visited[nx][ny] and graph[nx][ny] > 0:
                q.append((nx, ny))
                global_visited[nx][ny] = True
                
def count_zeros(i, j):
    zeros = 0
    dxs, dys = [0, 0, -1, 1], [1, -1, 0, 0]
    for dx, dy in zip(dxs, dys):
        nx = dx+i
        ny = dy+j
        if 0<=nx < N and 0<=ny<M and graph[nx][ny] == 0:
            zeros += 1
    return zeros

def count_division():
    global_visited = [[False for _ in range(M)] for _ in range(N)]
    count = 0
    for i in range(N):
        for j in range(M):
            if graph[i][j] > 0 and not global_visited[i][j]:
                count += 1
                bfs(i, j, global_visited)
    return count
time = 0
while True:
    zero_counts = [[0 for _ in range(M)] for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if graph[i][j] > 0:
                zero_counts[i][j] = count_zeros(i, j)
    left = False
    for i in range(N):
        for j in range(M):
            if graph[i][j] - zero_counts[i][j] > 0:
                graph[i][j] = graph[i][j] - zero_counts[i][j] 
                left = True
            else:
                graph[i][j] = 0
    if not left:
        print(0)
        break
    count = count_division()
    
    if count > 1:
        print(time+1)
        break
    time += 1