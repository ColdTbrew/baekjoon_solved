import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())
graph = [list(input().strip()) for _ in range(N)]

# 빨간 구슬(R)과 파란 구슬(B)의 초기 위치 찾기
ri, rj = 0, 0
bi, bj = 0, 0
for i in range(N):
    for j in range(M):
        if graph[i][j] == 'R':
            ri, rj = i, j
        elif graph[i][j] == 'B':
            bi, bj = i, j

# 방향: 상, 우, 하, 좌
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def steep(rx, ry, bx, by, direction):
    nrx, nry = rx, ry
    nbx, nby = bx, by
    red_moved, blue_moved = 0, 0  # 이동 거리 추적

    # 빨간 구슬 이동
    while True:
        next_rx = nrx + dx[direction]
        next_ry = nry + dy[direction]
        if graph[next_rx][next_ry] == '#':
            break
        nrx, nry = next_rx, next_ry
        red_moved += 1
        if graph[nrx][nry] == 'O':
            break
    
    # 파란 구슬 이동
    while True:
        next_bx = nbx + dx[direction]
        next_by = nby + dy[direction]
        if graph[next_bx][next_by] == '#':
            break
        nbx, nby = next_bx, next_by
        blue_moved += 1
        if graph[nbx][nby] == 'O':
            break
    
    # 겹침 처리: 이동 거리로 판단
    if nrx == nbx and nry == nby and graph[nrx][nry] != 'O':
        if direction == 0:  # 위쪽
            if rx > bx: nrx -= dx[direction]
            else: nbx -= dx[direction]
        elif direction == 1:  # 오른쪽
            if ry < by: nry -= dy[direction]
            else: nby -= dy[direction]
        elif direction == 2:  # 아래쪽
            if rx < bx: nrx -= dx[direction]
            else: nbx -= dx[direction]
        elif direction == 3:  # 왼쪽
            if ry > by: nry -= dy[direction]
            else: nby -= dy[direction]
    
    return nrx, nry, nbx, nby

def bfs():
    q = deque([(ri, rj, bi, bj, 0)])
    visited = set([(ri, rj, bi, bj)])

    while q:
        rx, ry, bx, by, cnt = q.popleft()

        if cnt > 10:
            return -1
        
        # 종료 조건
        red_in_hole = graph[rx][ry] == 'O'
        blue_in_hole = graph[bx][by] == 'O'
        
        if blue_in_hole:  # 파란 구슬이 구멍에 들어가면 실패
            continue
        if red_in_hole:  # 빨간 구슬만 구멍에 들어가면 성공
            return cnt
        
        for d in range(4):
            nrx, nry, nbx, nby = steep(rx, ry, bx, by, d)
            if (nrx, nry, nbx, nby) not in visited:
                visited.add((nrx, nry, nbx, nby))
                q.append((nrx, nry, nbx, nby, cnt + 1))
    
    return -1

print(bfs())