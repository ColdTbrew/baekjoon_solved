import sys
input = sys.stdin.readline

# 입력 처리
n = int(input().strip())  # 개행문자 제거
MOD = 10**9 + 7

# 행렬 곱셈
def matrix_mult(A, B):
    return [
        [(A[0][0] * B[0][0] + A[0][1] * B[1][0]) % MOD, (A[0][0] * B[0][1] + A[0][1] * B[1][1]) % MOD],
        [(A[1][0] * B[0][0] + A[1][1] * B[1][0]) % MOD, (A[1][0] * B[0][1] + A[1][1] * B[1][1]) % MOD]
    ]

# 행렬 제곱 (분할 정복)
def matrix_power(A, n):
    if n == 0:  # n=0: 단위 행렬
        return [[1, 0], [0, 1]]
    if n == 1:  # n=1: A 반환
        return [[x % MOD for x in row] for row in A]
    half = matrix_power(A, n // 2)
    if n % 2 == 0:
        return matrix_mult(half, half)
    return matrix_mult(matrix_mult(half, half), A)

# 피보나치 계산
if n == 0:
    print(0)
else:
    # 기본 행렬
    A = [[1, 1], [1, 0]]
    # A^(n-1) 계산
    result = matrix_power(A, n)
    # F(n) = result[1][0] (또는 result[0][1])
    print(result[1][0] % MOD)