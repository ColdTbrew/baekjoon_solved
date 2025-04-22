import sys
input = sys.stdin.readline

N = int(input())

# 격자 초기화 (N줄, 각 줄 길이 2N-1)
width = 2 * N - 1
grid = [[' ' for _ in range(width)] for _ in range(N)]

def draw_pattern(n, start_row, start_col):
    if n == 3:
        # N=3 기본 패턴
        grid[start_row][start_col + 2] = '*'  # * (가운데)
        grid[start_row + 1][start_col + 1] = '*'  # * *
        grid[start_row + 1][start_col + 3] = '*'
        grid[start_row + 2][start_col] = '*'  # *****
        grid[start_row + 2][start_col + 1] = '*'
        grid[start_row + 2][start_col + 2] = '*'
        grid[start_row + 2][start_col + 3] = '*'
        grid[start_row + 2][start_col + 4] = '*'
        return
    
    # 재귀적으로 상단과 하단 패턴 배치
    half = n // 2
    # 상단: N/2 패턴 (가운데 정렬)
    draw_pattern(half, start_row, start_col + half)
    # 하단: N/2 패턴을 좌우로 배치
    draw_pattern(half, start_row + half, start_col)
    draw_pattern(half, start_row + half, start_col + n)

# 패턴 그리기
draw_pattern(N, 0, 0)

# 출력
for row in grid:
    print(''.join(row))