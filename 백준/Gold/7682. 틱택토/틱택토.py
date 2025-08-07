import sys
import heapq
input = sys.stdin.readline


ans = []


def check(grid, t):
    # 가로, 세로 3줄
    for i in range(3):
        if grid[i][0] == grid[i][1] == grid[i][2] == t:
            return True
        if grid[0][i] == grid[1][i] == grid[2][i] == t:
            return True
    
    # 두 대각선
    if grid[0][0] == grid[1][1] == grid[2][2] == t:
        return True
    if grid[0][2] == grid[1][1] == grid[2][0] == t:
        return True

    return False
    
ans = []

while 1:
    case = input().strip()
    if case == "end":
        break
    else:
        grid = [list(case[i*3:i*3+3]) for i in range(3)]

        xcnt = case.count("X")
        ocnt = case.count("O")
        if not (xcnt == ocnt or xcnt == ocnt + 1):
            print("invalid")
            continue

        x_win = check(grid, "X")
        o_win = check(grid, "O")

        # 3. 승리 조건에 따른 유효성 검사
        if x_win and o_win:
            # X와 O가 동시에 이길 수는 없음
            print("invalid")
        elif x_win and xcnt == ocnt + 1:
            # X가 이겼다면, X는 O보다 하나 더 많아야 함
            print("valid")
        elif o_win and xcnt == ocnt:
            # O가 이겼다면, X와 O의 개수가 같아야 함
            print("valid")
        elif not x_win and not o_win and xcnt + ocnt == 9:
            # 승자가 없고 보드가 가득 찼을 때 (무승부)
            print("valid")
        else:
            # 그 외의 모든 경우는 invalid
            print("invalid")
