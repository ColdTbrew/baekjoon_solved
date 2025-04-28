import sys
from collections import deque
input = sys.stdin.readline

# 입력 처리
N = int(input())
grid = []
shark_pos = None  # 아기 상어 위치
for i in range(N):
    row = list(map(int, input().split()))
    grid.append(row)
    for j in range(N):
        if grid[i][j] == 9:
            shark_pos = (i, j)
            grid[i][j] = 0  # 아기 상어 위치를 빈 칸으로 설정

# 방향: 상, 좌, 하, 우
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

# BFS로 먹을 수 있는 물고기 탐색
def bfs(shark_x, shark_y, shark_size):
    visited = [[-1] * N for _ in range(N)]
    queue = deque([(shark_x, shark_y)])
    visited[shark_x][shark_y] = 0
    fish = []  # (거리, x, y) 형태로 먹을 수 있는 물고기 저장
    
    while queue:
        x, y = queue.popleft()
        for d in range(4):
            nx, ny = x + dx[d], y + dy[d]
            if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] == -1:
                # 아기 상어가 지나갈 수 있는 칸인지 확인
                if grid[nx][ny] <= shark_size:  # 크기가 같거나 작은 경우 (지나갈 수 있음)
                    visited[nx][ny] = visited[x][y] + 1
                    queue.append((nx, ny))
                    # 먹을 수 있는 물고기인지 확인
                    if 0 < grid[nx][ny] < shark_size:
                        fish.append((visited[nx][ny], nx, ny))
    
    if not fish:  # 먹을 물고기가 없으면
        return None
    # 거리, 행, 열 순으로 정렬 (우선순위: 거리 -> 행 -> 열)
    fish.sort()
    return fish[0]  # 가장 가까운 물고기 반환 (거리, x, y)

# 아기 상어 시뮬레이션
def simulate():
    shark_x, shark_y = shark_pos  # 아기 상어 초기 위치
    shark_size = 2  # 초기 크기
    eaten = 0  # 먹은 물고기 수
    total_time = 0  # 총 시간
    
    while True:
        # 먹을 수 있는 물고기 찾기
        result = bfs(shark_x, shark_y, shark_size)
        if result is None:  # 더 이상 먹을 물고기가 없으면 종료
            break
        
        # 물고기 먹기
        dist, fish_x, fish_y = result
        total_time += dist  # 이동 시간 추가
        grid[fish_x][fish_y] = 0  # 물고기 먹음 (빈 칸으로)
        shark_x, shark_y = fish_x, fish_y  # 아기 상어 이동
        
        # 크기 갱신
        eaten += 1
        if eaten == shark_size:  # 크기와 같은 수의 물고기를 먹으면 크기 증가
            shark_size += 1
            eaten = 0
    
    return total_time

# 결과 출력
print(simulate())