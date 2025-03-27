import sys
input = sys.stdin.readline

n = int(input())
count = 0
col = [0] * n  # 각 행의 퀸 위치
used_col = [False] * n  # 열 사용 여부
diag1 = [False] * (2 * n - 1)  # / 방향 대각선 (row + col)
diag2 = [False] * (2 * n - 1)  # \ 방향 대각선 (row - col + n - 1)

def n_queen(row):
    global count
    if row == n:
        count += 1
        return
    
    for i in range(n):
        if (not used_col[i] and 
            not diag1[row + i] and 
            not diag2[row - i + n - 1]):
            col[row] = i
            used_col[i] = True
            diag1[row + i] = True
            diag2[row - i + n - 1] = True
            n_queen(row + 1)
            # 백트래킹: 원상 복구
            used_col[i] = False
            diag1[row + i] = False
            diag2[row - i + n - 1] = False

n_queen(0)
print(count)