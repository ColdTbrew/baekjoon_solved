n, m = list(map(int, input().split()))

board = [["" for _ in range(m)] for _ in range(n)]

for i in range(n):
    row = input()
    for j in range(m):
        board[i][j] = row[j]

# 8*8 은64개중에 그러면 W가 32개랑 가까우면됨
to_color = 64
for start_i in range(n-7):
    for start_j in range(m-7):
        c_w = 0
        c_b = 0
        for i in range(8):
            for j in range(8):
                curr = board[start_i+i][start_j+j]
                if (i+j) % 2 == 0:
                    if curr != "W":
                        c_w += 1
                    if curr != "B":
                        c_b += 1
                else:
                    if curr != "B":
                        c_w += 1
                    if curr != "W":
                        c_b += 1
        to_color = min(to_color, c_w, c_b)
print(to_color)