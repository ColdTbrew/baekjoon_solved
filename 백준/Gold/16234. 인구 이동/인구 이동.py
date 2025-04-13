import sys
from collections import deque
input = sys.stdin.readline

# 입력 처리
N, L, R = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]

# 방향: 상, 우, 하, 좌
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

def bfs(start_x, start_y, visited):
    queue = deque([(start_x, start_y)])
    visited[start_y][start_x] = True
    union = [(start_x, start_y)]  # 연합 좌표
    total_pop = A[start_y][start_x]  # 연합 인구 합
    count = 1  # 연합 칸 수
    
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < N and 0 <= ny < N and not visited[ny][nx]:
                # 인구 차이 조건 확인
                if L <= abs(A[y][x] - A[ny][nx]) <= R:
                    queue.append((nx, ny))
                    visited[ny][nx] = True
                    union.append((nx, ny))
                    total_pop += A[ny][nx]
                    count += 1
    
    # 연합 정보 반환
    return union, total_pop, count

def move_population():
    day = 0
    while True:
        visited = [[False] * N for _ in range(N)]
        unions = []  # 모든 연합 저장
        moved = False  # 인구 이동 여부
        
        # 모든 칸 탐색
        for y in range(N):
            for x in range(N):
                if not visited[y][x]:
                    union, total_pop, count = bfs(x, y, visited)
                    if count > 1:  # 연합 크기가 2 이상
                        unions.append((union, total_pop, count))
                        moved = True
        
        # 인구 이동 없으면 종료
        if not moved:
            break
        
        # 연합별 인구 이동
        for union, total_pop, count in unions:
            new_pop = total_pop // count
            for x, y in union:
                A[y][x] = new_pop
        
        day += 1
    
    return day

# 결과 출력
print(move_population())