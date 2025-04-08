import sys
from collections import deque
import copy

input = sys.stdin.readline

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]

# 방향: 상, 우, 하, 좌
dx = [-1, 0, 1, 0]  # x 변화: 상(-1), 우(0), 하(1), 좌(0)
dy = [0, 1, 0, -1]  # y 변화: 상(0), 우(1), 하(0), 좌(-1)

def move(board, direction):
    new_board = [[0] * N for _ in range(N)]
    merged = [[False] * N for _ in range(N)]

    # 방향에 따른 시작점과 순서 설정
    if direction == 0:  # 상: 위에서 아래로 순회
        start_x, end_x, step_x = 0, N, 1
        start_y, end_y, step_y = 0, N, 1
    elif direction == 1:  # 우: 오른쪽에서 왼쪽으로 순회
        start_x, end_x, step_x = 0, N, 1
        start_y, end_y, step_y = N-1, -1, -1
    elif direction == 2:  # 하: 아래에서 위로 순회
        start_x, end_x, step_x = N-1, -1, -1
        start_y, end_y, step_y = 0, N, 1
    elif direction == 3:  # 좌: 왼쪽에서 오른쪽으로 순회
        start_x, end_x, step_x = 0, N, 1
        start_y, end_y, step_y = 0, N, 1

    for i in range(start_x, end_x, step_x):
        for j in range(start_y, end_y, step_y):
            if board[i][j] == 0:
                continue
            x, y = i, j
            while True:
                nx = x + dx[direction]
                ny = y + dy[direction]
                # 범위를 벗어나면 현재 위치에 저장
                if not (0 <= nx < N and 0 <= ny < N):
                    new_board[x][y] = board[i][j]
                    break
                # 빈 칸이면 이동
                if new_board[nx][ny] == 0:
                    x, y = nx, ny
                # 같은 값이고 합쳐지지 않았으면 합치기
                elif new_board[nx][ny] == board[i][j] and not merged[nx][ny]:
                    new_board[nx][ny] = board[i][j] * 2
                    merged[nx][ny] = True
                    break
                # 다른 값이거나 이미 합쳐졌으면 현재 위치에 저장
                else:
                    new_board[x][y] = board[i][j]
                    break
    return new_board

def dfs(board, depth):
    if depth == 5:
        return max(max(row) for row in board)
    
    max_block = 0
    for d in range(4):
        new_board = move(copy.deepcopy(board), d)
        max_block = max(max_block, dfs(new_board, depth + 1))

    return max_block

print(dfs(board, 0))