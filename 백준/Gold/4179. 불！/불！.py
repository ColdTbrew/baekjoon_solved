R, C = map(int, input().split())

miro = []

for _ in range(R):
    row = list(input().strip())
    miro.append(row)

dxs, dys = [0,0,-1,1], [-1, 1,0,0]

from collections import deque


time = 0

jihun_q = deque()
fire_q = deque()
visited = [[-1] * C for _ in range(R)] # 방문시간 저장

for i in range(R):
    for j in range(C):
        if miro[i][j] == 'J':
            jihun_q.append((i, j, 0))
            visited[i][j] = 0
        elif miro[i][j] == 'F':
            fire_q.append((i, j))

def bfs():
    while jihun_q:
        # 1. 불 확산 (지훈이 이동 전에 불이 먼저 번짐)
        fire_moves_count = len(fire_q)
        for _ in range(fire_moves_count):
            x, y = fire_q.popleft()
            for i in range(4):
                nx, ny = x + dxs[i], y + dys[i]
                if 0 <= nx < R and 0 <= ny < C and miro[nx][ny] == '.':
                    miro[nx][ny] = 'F'
                    fire_q.append((nx, ny))

        # 2. 지훈이 이동
        jihun_moves_count = len(jihun_q)
        for _ in range(jihun_moves_count):
            x, y, time = jihun_q.popleft()
            
            # 탈출 조건: 미로의 가장자리에 도달
            if x == 0 or x == R - 1 or y == 0 or y == C - 1:
                return time + 1

            for i in range(4):
                nx, ny = x + dxs[i], y + dys[i]
                
                # 다음 위치가 미로 범위 내에 있고, 벽이 아니며,
                # 불이 아닌 일반 공간이고, 아직 방문하지 않았다면 이동
                if 0 <= nx < R and 0 <= ny < C and miro[nx][ny] == '.' and visited[nx][ny] == -1:
                    visited[nx][ny] = time + 1
                    jihun_q.append((nx, ny, time + 1))
    
    return "IMPOSSIBLE"
    # while fire_q:
    #     x, y = fire_q.popleft()
    #     for dx, dy in zip(dxs, dys):
    #         nx, ny = dx+x, dy+y
    #         if 0<= nx < R and 0<=ny <C and miro[nx][ny] != '#' and miro[nx][ny] != 'F':
    #                 miro[nx][ny] = 'F'
    #                 fire_q.append((nx, ny))
    # while jihun_q:
    #     x, y, time = jihun_q.popleft()
    #     for i in range(4):
    #         nx, ny = x + dxs[i], y+dys[i]
    #         if nx <0 or nx >= R or ny<0 or ny>=C:
    #             return time + 1
    #         if miro[nx][ny] == '.' and visited[nx][ny] == -1: #빈곳이고 안방문했다면
    #             if miro[nx][ny] != 'F': # 불이 아니여야하고 
    #                 visited[nx][ny] = time + 1
    #                 jihun_q.append((nx, ny,  time+1))
    # return "IMPOSSIBLE"
print(bfs())