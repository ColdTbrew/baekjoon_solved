import sys

R, C, N = map(int, input().split())
grid = [list(input().strip()) for _ in range(R)]

times = [[-1] * C for _ in range(R)]
for i in range(R):
    for j in range(C):
        if grid[i][j] == 'O':
            times[i][j] = 0

for t in range(1, N + 1):
    if t % 2 == 0 and t >= 2:
        for i in range(R):
            for j in range(C):
                if times[i][j] == -1:
                    times[i][j] = t
    elif t % 2 == 1 and t >= 3:
        to_destroy = set()
        for i in range(R):
            for j in range(C):
                if times[i][j] == t - 3:
                    to_destroy.add((i, j))
                    for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                        ni, nj = i + di, j + dj
                        if 0 <= ni < R and 0 <= nj < C:
                            to_destroy.add((ni, nj))
        for pi, pj in to_destroy:
            times[pi][pj] = -1

for i in range(R):
    row = ['O' if times[i][j] != -1 else '.' for j in range(C)]
    print(''.join(row))