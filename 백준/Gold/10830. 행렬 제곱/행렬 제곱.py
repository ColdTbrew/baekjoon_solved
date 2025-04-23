import sys
input = sys.stdin.readline

N, B = map(int, input().split())
mat = [[]*N for _ in range(N)]
for i in range(N):
    row = list(map(int, input().split()))
    mat[i] = row

# mat * B
# (A×B)[i][j] = Σ(A[i][k] × B[k][j])
def mult(A, B, N):
    result = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            for k in range(N):
                result[i][j] += (A[i][k] * B[k][j])%1000
                result[i][j] = result[i][j]%1000
    return result

def power(A, B, N):
    if B==1:
        return [[x%1000 for x in row] for row in A]
    
    half = power(A, B//2 , N)
    half_square = mult(half, half, N)
    if B%2 == 0: #짝수
        return half_square
    else:
        return mult(half_square, A, N)

result = power(mat, B, N)

for row in result:
    print(*row)