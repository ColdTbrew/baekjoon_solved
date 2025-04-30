# 행렬 입력
N, M = map(int, input().split())
A = [list(map(int, input().strip())) for _ in range(N)]
B = [list(map(int, input().strip())) for _ in range(N)]

# 3x3 연산 함수
def flip(matrix, i, j):
    for x in range(i, i+3):
        for y in range(j, j+3):
            matrix[x][y] = 1 - matrix[x][y]  # 0 ↔ 1 뒤집기

# A == B 확인 함수
def is_same(A, B, N, M):
    return all(A[i][j] == B[i][j] for i in range(N) for j in range(M))

# 그리디 알고리즘
count = 0
if N < 3 or M < 3:
    # 3x3 연산 불가능, A == B 여부만 확인
    if is_same(A, B, N, M):
        print(0)
    else:
        print(-1)
else:
    # 왼쪽 위부터 순회
    for i in range(N-2):
        for j in range(M-2):
            if A[i][j] != B[i][j]:
                flip(A, i, j)  # 3x3 연산 적용
                count += 1
    
    # 최종 확인
    if is_same(A, B, N, M):
        print(count)
    else:
        print(-1)