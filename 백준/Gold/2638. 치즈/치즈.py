import sys
input = sys.stdin.readline
from collections import deque

N, M = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]

def get_exposed():
    a = []
    dxs, dys = [0, 0, -1, 1], [-1, 1, 0, 0]

    for i in range(N):
        for j in range(M):
            if grid[i][j] == 1:
                count = 0
                for dx, dy in zip(dxs, dys):
                    nx, ny = i+dx, j+dy
                    if 0<=nx < N and 0<=ny<M and grid[nx][ny] == 2:
                        count += 1
                if count >= 2:
                    a.append((i, j))
    return a

def cheese_left():
    for i in range(N):
        for j in range(M):
            if grid[i][j] == 1:
                return True
    return False
def view():
    for i in grid:
        print(i)
    print()
def melt(cheese):
    for i, j in cheese:
        grid[i][j] = 0
def aired():
    q = deque()
    q.append((0, 0))
    dxs, dys = [0, 0, -1, 1], [-1, 1, 0, 0]
    visited = [ [0] * M for _ in range(N)]
    visited[0][0] = True
    grid[0][0] = 2
    while q:
        i , j = q.popleft()
        for dx, dy in zip(dxs, dys):
            nx, ny = i + dx, j + dy
            if 0<= nx < N and 0<=ny < M and grid[nx][ny] != 1 and not visited[nx][ny]:
                grid[nx][ny] = 2
                visited[nx][ny] = True
                q.append((nx, ny))
T = 0
while cheese_left():
    T += 1
    aired()
    # view()
    exposed_cheese = get_exposed()
    if not exposed_cheese:
        break
    melt(exposed_cheese)

print(T)