import sys 
input = sys.stdin.readline

board = [list(map(int, list(input().strip()))) for _ in range(9)]
# print(board)


blanks = []
for i in range(9):
    for j in range(9):
        if board[i][j] == 0:
            blanks.append((i, j))

def can_place(x, y, num):
    #행확인, 열확인, 박스확인
    for j in range(9):
        if board[x][j] == num:
            return False
    for i in range(9):
        if board[i][y] == num:
            return False
        
    starx, stary = (x//3)*3 , (y//3)*3

    for i in range(starx, starx+3):
        for j in range(stary, stary+3):
            if board[i][j] == num:
                return False
    return True

def solve(idx):
    if idx == len(blanks):
        for row in board:
            print(*row, sep="")
        return True
    x, y = blanks[idx]
    for num in range(1, 10):
        if can_place(x, y, num):
            board[x][y] = num
            if solve(idx + 1):
                return True
            board[x][y] = 0
    return False

solve(0)