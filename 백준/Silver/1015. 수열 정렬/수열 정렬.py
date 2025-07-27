# 입력
N = int(input())
A = list(map(int, input().split()))

# (값, 원래 인덱스) 쌍을 저장
A_with_index = [(A[i], i) for i in range(N)]

# 값 기준 오름차순 정렬, 값이 같으면 인덱스 기준 오름차순
A_with_index.sort()

# P 배열 생성
P = [0] * N
for i in range(N):
    P[A_with_index[i][1]] = i  # 원래 인덱스에 정렬된 순서(0, 1, 2, ...)를 배치

# 결과 출력
print(*P)