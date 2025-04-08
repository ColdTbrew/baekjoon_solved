import sys
input = sys.stdin.readline

N, M = map(int, input().split())

r, c, d = map(int, input().split())

graph = [[] * M for _ in range(N)]
for i in range(N):
    row = list(map(int, input().split()))
    graph[i] = row

from collections import deque

visited = [[False] * M for _ in range(N)]

dx = [-1, 0, 1, 0]  # 북, 동, 남, 서
dy = [0, 1, 0, -1]

# 청소한 칸 체크
visited = [[False] * M for _ in range(N)]
count = 0  # 청소한 칸 수

# 현재 위치와 방향
x, y, direction = r, c, d

while True:
    # 1. 현재 칸 청소
    if not visited[x][y]:
        visited[x][y] = True
        count += 1
    
    # 2. 주변 4칸 확인
    empty = False
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < N and 0 <= ny < M and graph[nx][ny] == 0 and not visited[nx][ny]:
            empty = True
            break
    
    # 2-1. 청소되지 않은 빈 칸이 없는 경우
    if not empty:
        # 후진 방향 계산
        back_dir = (direction + 2) % 4
        bx = x + dx[back_dir]
        by = y + dy[back_dir]
        # 후진 가능하면 후진
        if 0 <= bx < N and 0 <= by < M and graph[bx][by] != 1:
            x, y = bx, by
            continue
        # 후진 불가능하면 종료
        else:
            break
    
    # 3. 청소되지 않은 빈 칸이 있는 경우
    else:
        # 반시계 90도 회전
        direction = (direction - 1) % 4
        # 앞쪽이 청소되지 않은 빈 칸이면 전진
        nx = x + dx[direction]
        ny = y + dy[direction]
        if 0 <= nx < N and 0 <= ny < M and graph[nx][ny] == 0 and not visited[nx][ny]:
            x, y = nx, ny

print(count)