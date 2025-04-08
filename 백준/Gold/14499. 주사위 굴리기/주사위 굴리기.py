import sys
input = sys.stdin.readline

N, M, x, y, K = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
cmds = list(map(int, input().split()))

# 동(1), 서(2), 북(3), 남(4) -> 인덱스 0, 1, 2, 3
dx = [0, 0, -1, 1]  # 동, 서, 북, 남
dy = [1, -1, 0, 0]

# 주사위 면: [위, 북, 동, 남, 서, 아래]
dice = [0, 0, 0, 0, 0, 0]  # 초기값 0

def roll_dice(d, dice):
    # 방향에 따른 주사위 면 변화
    if d == 0:  # 동: 위→동, 동→아래, 아래→서, 서→위
        dice[0], dice[2], dice[5], dice[4] = dice[2], dice[5], dice[4], dice[0]
    elif d == 1:  # 서: 위→서, 서→아래, 아래→동, 동→위
        dice[0], dice[4], dice[5], dice[2] = dice[4], dice[5], dice[2], dice[0]
    elif d == 2:  # 북: 위→북, 북→아래, 아래→남, 남→위
        dice[0], dice[1], dice[5], dice[3] = dice[1], dice[5], dice[3], dice[0]
    elif d == 3:  # 남: 위→남, 남→아래, 아래→북, 북→위
        dice[0], dice[3], dice[5], dice[1] = dice[3], dice[5], dice[1], dice[0]

    
    return dice

for cmd in cmds:
    d = cmd - 1  # 명령을 0-based로 변환
    nx = x + dx[d]
    ny = y + dy[d]
    
    # 경계 체크: 이동 불가 시 무시
    if not (0 <= nx < N and 0 <= ny < M):
        continue
    
    # 이동
    x, y = nx, ny
    
    # 주사위 굴리기
    dice = roll_dice(d, dice)
    
    # 바닥면(5)과 지도 상호작용
    if graph[x][y] == 0:
        graph[x][y] = dice[5]
    else:
        dice[5] = graph[x][y]
        graph[x][y] = 0
    
    # 윗면(0) 출력
    print(dice[0])