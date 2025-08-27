import sys

H, W, X, Y = map(int, sys.stdin.readline().strip().split())

B = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(H+X)]

for i in range(X,H):
    for j in range(Y,W):
        B[i][j] = B[i][j] - B[i-X][j-Y]

for result in B[:H]:
    print(*result[:W])