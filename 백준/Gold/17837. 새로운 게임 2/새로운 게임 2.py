import sys

# 체스판의 크기 N, 말의 개수 K 입력
N, K = map(int, sys.stdin.readline().split())

dxs = [0, 0, -1, 1]
dys = [1, -1, 0, 0]

# 체스판 정보 입력 (0:흰색, 1:빨간색, 2:파란색)
board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

# 각 말의 정보 [행, 열, 방향]을 저장하는 리스트
horses = []
# 체스판 각 칸의 말 쌓임 상태를 저장하는 2차원 리스트
board_state = [[[] for _ in range(N)] for _ in range(N)]

# K개의 말 정보 입력 및 초기화
for i in range(K):
    # 행, 열, 방향을 0-indexed로 변환하여 저장
    x, y, d = map(int, sys.stdin.readline().split())
    horses.append([x - 1, y - 1, d - 1])
    board_state[x - 1][y - 1].append(i)

# 특정 말과 그 위의 모든 말을 이동시키는 함수
def move_stack(horse_idx, nx, ny):
    # 이동을 시작하는 말의 현재 위치
    x, y, d = horses[horse_idx]
    stack_pos = board_state[x][y].index(horse_idx)
    
    to_move = board_state[x][y][stack_pos:]
    
    board_state[x][y] = board_state[x][y][:stack_pos]
    
    # 이동하려는 칸이 빨간색(1)인 경우, 이동할 말들의 순서를 뒤집음
    if board[nx][ny] == 1:
        to_move.reverse()
        
    for h_idx in to_move:
        horses[h_idx][0], horses[h_idx][1] = nx, ny
        board_state[nx][ny].append(h_idx)
        
    if len(board_state[nx][ny]) >= 4:
        return True
    return False

for turn in range(1, 1001):
    for i in range(K):
        x, y, d = horses[i]
        

        nx, ny = x + dxs[d], y + dys[d]
        
        if not (0 <= nx < N and 0 <= ny < N) or board[nx][ny] == 2:

            if d in [0, 2]: d += 1
            elif d in [1, 3]: d -= 1
            horses[i][2] = d
            
            nx, ny = x + dxs[d], y + dys[d]
            
            if not (0 <= nx < N and 0 <= ny < N) or board[nx][ny] == 2:
                continue

        if move_stack(i, nx, ny):
            print(turn)
            sys.exit()

print(-1)