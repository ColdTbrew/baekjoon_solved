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
        pos = i
        for j in range(H):
            if pos < N-1 and sadari[j][pos] == 1:
                pos += 1
            elif pos > 0 and sadari[j][pos-1] == 1:
                pos -= 1
        if pos != i:
            return False
    return True

# DFS: 최소 가로선 수 탐색
def dfs(cnt, start):
    global answer
    if cnt >= answer: # 이미 작은 answer로 성공
        return
    if bebero(): # 가능한 사다리라서 정답 갱신
        answer = cnt
        return
    if cnt == 3: # 가로선 3개 초과는 피요없음
        return
    for i in range(start, H):
        for j in range(N-1):
            if (sadari[i][j] == 0 and
                (j == 0 or sadari[i][j-1] == 0) and
                (j == N-2 or sadari[i][j+1] == 0)):
                sadari[i][j] = 1
                dfs(cnt+1, i)
                sadari[i][j] = 0

# 실행
answer = 4
dfs(0, 0)
print(-1 if answer > 3 else answer)
