import sys
input = sys.stdin.readline

# 격자 크기 입력
N, M = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]

# 테트로미노 모양 정의 (각 모양의 상대 좌표)
tetrominoes = [
    # ㅡ (I 모양)
    [(0,0), (0,1), (0,2), (0,3)],
    [(0,0), (1,0), (2,0), (3,0)],

    # ㅁ (O 모양)
    [(0,0), (0,1), (1,0), (1,1)],

    # L 모양
    [(0,0), (1,0), (2,0), (2,1)],
    [(0,0), (0,1), (0,2), (1,0)],
    [(0,0), (0,1), (1,1), (2,1)],
    [(0,2), (1,0), (1,1), (1,2)],

    # L 대칭 (J 모양)
    [(0,1), (1,1), (2,1), (2,0)],
    [(0,0), (1,0), (1,1), (1,2)],
    [(0,0), (0,1), (1,0), (2,0)],
    [(0,0), (0,1), (0,2), (1,2)],

    # ㅗ (T 모양)
    [(0,0), (0,1), (0,2), (1,1)],
    [(0,1), (1,0), (1,1), (2,1)],
    [(0,1), (1,0), (1,1), (1,2)],
    [(0,0), (1,0), (1,1), (2,0)],

    # S 모양
    [(0,1), (0,2), (1,0), (1,1)],
    [(0,0), (1,0), (1,1), (2,1)],

    # Z 모양
    [(0,0), (0,1), (1,1), (1,2)],
    [(0,1), (1,0), (1,1), (2,0)],
]


# 격자 범위 내에 있는지 확인
def is_valid(x, y):
    return 0 <= x < N and 0 <= y < M

# 테트로미노를 놓았을 때 합 계산
def calc_sum(x, y, tetromino):
    total = 0
    for dx, dy in tetromino:
        nx, ny = x + dx, y + dy
        if not is_valid(nx, ny):
            return -1  # 범위를 벗어나면 불가능
        total += grid[nx][ny]
    return total

# 최대 합 찾기
max_sum = 0
for i in range(N):
    for j in range(M):
        for tetromino in tetrominoes:
            result = calc_sum(i, j, tetromino)
            if result != -1:
                max_sum = max(max_sum, result)

print(max_sum)