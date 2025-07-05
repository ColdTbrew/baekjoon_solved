import sys
D = int(sys.stdin.readline())
mod = 1_000_000_007
N = 8

def multiply(mat1, mat2):
    res = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            for k in range(N):
                res[i][j] += mat1[i][k] * mat2[k][j]  # 누적
                res[i][j] %= mod  # 각 계산마다 모듈러 연산
    return res

def power(matrix, exp):
    res = [[1 if i == j else 0 for j in range(N)] for i in range(N)]  # 단위 행렬
    base = matrix
    while exp > 0:
        if exp % 2 == 1:
            res = multiply(res, base)
        base = multiply(base, base)
        exp //= 2
    return res

def solve():
    adj_matrix = [
        [0, 1, 1, 0, 0, 0, 0, 0],  # 정보과학관
        [1, 0, 1, 1, 0, 0, 0, 0],  # 전산관
        [1, 1, 0, 1, 0, 1, 0, 0],  # 미래관
        [0, 1, 1, 0, 1, 1, 0, 0],  # 신양관
        [0, 0, 0, 1, 0, 1, 0, 1],  # 진리관
        [0, 0, 1, 1, 1, 0, 1, 0],  # 한경직기념관
        [0, 0, 0, 0, 0, 1, 0, 1],  # 형남공학관
        [0, 0, 0, 0, 1, 0, 1, 0]   # 학생회관
    ]

    result = power(adj_matrix, D)
    print(result[0][0])  # 정보과학관에서 시작해 정보과학관으로 돌아오는 경로 수

solve()