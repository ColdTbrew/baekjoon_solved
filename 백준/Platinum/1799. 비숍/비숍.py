import sys
sys.setrecursionlimit(10000)

N = int(input())
board = []
for _ in range(N):
    board.append(list(map(int, input().split())))

# 흑백 칸 분리를 위한 두 개의 ans 변수
max_bishops_even_sum = 0 # (row + col)이 짝수인 칸 (i+j 대각선 번호가 짝수)
max_bishops_odd_sum = 0  # (row + col)이 홀수인 칸 (i+j 대각선 번호가 홀수)

# i-j 대각선 방문 여부 (총 2N-1개). N-1을 더해서 인덱스를 0부터 시작하게 함.
# 예: N=5일 때, r-c는 -4 ~ 4. 인덱스는 0 ~ 8 (총 9개)
visited_diff_diag = [False] * (2 * N - 1)

# 각 i+j 대각선에 놓을 수 있는 유효한 칸들 저장
# lst[k]는 (row, col) 쌍들의 리스트로, row + col == k 인 칸들
# k는 0부터 2*N-2까지 가능하므로, 크기는 2*N-1
valid_spots_on_diag_sum = [[] for _ in range(2 * N - 1)]

for r in range(N):
    for c in range(N):
        if board[r][c] == 1:
            valid_spots_on_diag_sum[r + c].append((r, c))

# L은 i+j 대각선 번호의 최대값 + 1, 즉 2*N-1 (대각선 번호의 개수)
# k는 이 대각선 번호를 나타내는 인덱스로 사용됨.
# dfs(k, cnt) 에서 k는 현재 처리할 i+j 대각선 번호를 의미
# cnt는 현재까지 놓은 비숍의 개수
def dfs_optimized(k, cnt, current_max_bishops_ref):
    global visited_diff_diag

    # 가지치기: 현재까지 찾은 최대값보다 더 좋게 될 가능성이 없다면 중단
    # L = 2*N-1. (L - k)는 남은 대각선의 개수.
    # (L - k + 1) // 2는 남은 대각선 중 최대로 놓을 수 있는 비숍의 개수를 대략적으로 추정
    # 왜 (L - k + 1) // 2 이냐면, k, k+2, k+4 ... 이런 식으로 두 칸씩 건너뛰기 때문
    if current_max_bishops_ref[0] >= (cnt + (2*N - 1 - k + 1) // 2): # L 대신 2*N-1 사용
        return

    # 모든 대각선 탐색 완료 (k가 마지막 대각선 번호 2*N-2를 넘어가면)
    if k >= (2 * N - 1): # 2*N-1이 마지막 대각선 번호 2N-2를 넘어선 경우
        current_max_bishops_ref[0] = max(current_max_bishops_ref[0], cnt)
        return

    # 현재 대각선 번호 k에 있는 유효한 칸들에 대해 비숍을 놓아보기
    for r, c in valid_spots_on_diag_sum[k]:
        # r-c 대각선에 비숍이 없는 경우에만 놓을 수 있음
        if not visited_diff_diag[r - c + N - 1]:
            visited_diff_diag[r - c + N - 1] = True  # 비숍 놓음 표시
            # 다음 대각선 (k+2)로 이동 (같은 색깔의 다음 대각선)
            dfs_optimized(k + 2, cnt + 1, current_max_bishops_ref)
            visited_diff_diag[r - c + N - 1] = False # 백트래킹 (비숍 치움)

    # 현재 대각선 번호 k에서 비숍을 하나도 놓지 않고 다음 대각선 (k+2)로 이동
    dfs_optimized(k + 2, cnt, current_max_bishops_ref)


# ----------------------------------------------------------------------
# 1. (row + col) 합이 짝수인 대각선들 탐색 (k = 0, 2, 4 ...)
# max_bishops_even_sum을 리스트로 감싸서 함수 내에서 참조하여 수정할 수 있도록 함
even_sum_container = [0]
dfs_optimized(0, 0, even_sum_container)
max_bishops_even_sum = even_sum_container[0]

# 대각선 방문 배열 초기화 (홀수 합 대각선 탐색을 위해)
visited_diff_diag = [False] * (2 * N - 1)

# 2. (row + col) 합이 홀수인 대각선들 탐색 (k = 1, 3, 5 ...)
odd_sum_container = [0]
dfs_optimized(1, 0, odd_sum_container)
max_bishops_odd_sum = odd_sum_container[0]

# 최종 결과 출력
print(max_bishops_even_sum + max_bishops_odd_sum)