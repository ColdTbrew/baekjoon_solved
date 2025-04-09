import sys
from collections import deque

input = sys.stdin.readline

# 입력 처리
N, M = map(int, input().split())
lab = [list(map(int, input().split())) for _ in range(N)]

# 빈 칸 좌표 수집
empty_cells = []
for i in range(N):
    for j in range(M):
        if lab[i][j] == 0:
            empty_cells.append((i, j))

# 방향 배열
dx = [-1, 1, 0, 0]  # 상, 하, 좌, 우
dy = [0, 0, -1, 1]

# BFS로 바이러스 확산
def spread_virus(temp_lab):
    queue = deque()
    visited = [[False] * M for _ in range(N)]
    
    # 모든 바이러스 위치에서 시작
    for i in range(N):
        for j in range(M):
            if temp_lab[i][j] == 2:
                queue.append((i, j))
                visited[i][j] = True
    
    while queue:
        x, y = queue.popleft()
        for d in range(4):
            nx, ny = x + dx[d], y + dy[d]
            if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny] and temp_lab[nx][ny] == 0:
                temp_lab[nx][ny] = 2
                visited[nx][ny] = True
                queue.append((nx, ny))

# 안전 영역 계산
def get_safe_area(lab):
    return sum(row.count(0) for row in lab)

# 벽 3개 선택 조합 생성 (재귀)
def generate_combinations(empty_cells, selected, start, max_safe_area):
    # 벽 3개가 선택된 경우
    if len(selected) == 3:
        # 지도 복사
        temp_lab = [row[:] for row in lab]
        
        # 벽 설치
        for x, y in selected:
            temp_lab[x][y] = 1
        
        # 바이러스 확산
        spread_virus(temp_lab)
        
        # 안전 영역 계산
        safe_area = get_safe_area(temp_lab)
        
        # 최대값 갱신 ( nonlocal 사용 대신 리스트로 전달 )
        max_safe_area[0] = max(max_safe_area[0], safe_area)
        return
    
    # 빈 칸을 순회하며 조합 생성
    for i in range(start, len(empty_cells)):
        selected.append(empty_cells[i])
        generate_combinations(empty_cells, selected, i + 1, max_safe_area)
        selected.pop()

# 최대 안전 영역 찾기
max_safe_area = [0]  # 리스트로 감싸서 재귀 내에서 갱신
generate_combinations(empty_cells, [], 0, max_safe_area)

# 결과 출력
print(max_safe_area[0])