import sys
input = sys.stdin.readline

# 입력 처리
N, L = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(N)]

# 길의 개수
answer = 0

# 경사로 설치 가능 여부 확인 함수
def can_pass(line):
    visited = [False] * N  # 경사로가 이미 설치된 위치 체크
    for i in range(N-1):
        if line[i] == line[i+1]:  # 높이가 같으면 계속 진행
            continue
        diff = line[i] - line[i+1]
        if abs(diff) != 1:  # 높이 차이가 1이 아니면 불가능
            return False
        
        if diff == 1:  # 현재가 더 높음 (오른쪽에 경사로 설치)
            if i + L >= N:  # 경사로가 범위를 벗어나면 불가능
                return False
            # 경사로 설치 구간의 높이가 모두 같고, 겹치지 않아야 함
            for j in range(i+1, i+1+L):
                if line[j] != line[i+1] or visited[j]:
                    return False
                visited[j] = True
        elif diff == -1:  # 다음이 더 높음 (왼쪽에 경사로 설치)
            if i - L + 1 < 0:  # 경사로가 범위를 벗어나면 불가능
                return False
            # 경사로 설치 구간의 높이가 모두 같고, 겹치지 않아야 함
            for j in range(i-L+1, i+1):
                if line[j] != line[i] or visited[j]:
                    return False
                visited[j] = True
    return True

# 가로 길 검사
for i in range(N):
    if can_pass(maps[i]):
        answer += 1

# 세로 길 검사
for j in range(N):
    col = [maps[i][j] for i in range(N)]  # 열을 리스트로 추출
    if can_pass(col):
        answer += 1

# 결과 출력
print(answer)