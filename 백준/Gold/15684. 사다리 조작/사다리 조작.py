import sys
input = sys.stdin.readline

# 입력 처리
N, M, H = map(int, input().split())
sadari = [[0] * N for _ in range(H)]

for _ in range(M):
    a, b = map(int, input().split())
    sadari[a-1][b-1] = 1

# 경로 확인: 모든 세로선 i가 i로 끝나는지
def bebero():
    for i in range(N):
        start_num = i
        for j in range(H):
            if start_num < N-1 and sadari[j][start_num] == 1:
                start_num += 1
            elif start_num > 0 and sadari[j][start_num-1] == 1:
                start_num -= 1
        if i != start_num:
            return False
    return True

# 가로선 추가 가능 여부
def can_add_ladder(i, j):
    if sadari[i][j] == 1:
        return False
    if j > 0 and sadari[i][j-1] == 1:
        return False
    if j < N-2 and sadari[i][j+1] == 1:
        return False
    return True

# DFS: 최소 가로선 수 탐색
def dfs(cnt, x, y):
    global answer
    # 현재 추가한 가로선 수가 답보다 크면 종료
    if answer <= cnt:
        return
    # 경로가 올바르면 답 갱신
    if bebero():
        answer = min(answer, cnt)
        return
    # 최대 3개까지만 추가
    if cnt >= 3:
        return
    # (x, y)부터 유효한 위치 탐색
    for i in range(x, H):
        # j는 y부터 시작 (같은 행일 때만)
        start_j = y if i == x else 0
        for j in range(start_j, N-1):
            if can_add_ladder(i, j):
                sadari[i][j] = 1
                # 다음 위치는 같은 행의 j+2 또는 다음 행
                next_i, next_j = (i, j+2) if j+2 < N-1 else (i+1, 0)
                dfs(cnt+1, next_i, next_j)
                sadari[i][j] = 0
                # 연속 탐색 방지 (j+1은 이미 체크했으므로 j+2로 이동)
                j += 1

# 초기화 및 실행
answer = 4
dfs(0, 0, 0)
print(-1 if answer > 3 else answer)