import sys
input = sys.stdin.readline

N = int(input().strip())
K = int(input().strip())

board = [[0] * N for _ in range(N)]
for _ in range(K):
    i, j = map(int, input().split())
    board[i-1][j-1] = 1

L = int(input().strip())


direction = 1
dxs, dys = [-1, 0, 1, 0], [0,1,0,-1] #상, 우, 하, 좌

from collections import deque

moves = []
for _ in range(L):
    time, cmd = input().split()
    time = int(time)
    moves.append((time, cmd))

snack = deque([(0,0)])
total_time = 0
def simulate():
    global total_time, direction
    move_idx = 0
    while True:
        total_time += 1
        x, y = snack[-1]
        nx = x + dxs[direction]
        ny = y + dys[direction]
        if not (0 <= nx < N and 0<=ny<N) or (nx,ny) in snack:
            return total_time
        # 머리 추가
        snack.append((nx, ny))

        if board[nx][ny] == 1:
            board[nx][ny] = 0
        else:
            snack.popleft() # 꼬리 제거
        
        if move_idx < L and total_time == moves[move_idx][0]:
            cmd = moves[move_idx][1]
            if cmd == 'L':
                direction = (direction-1)%4
            elif cmd == 'D':
                direction = (direction+1)%4
            move_idx += 1


print(simulate())