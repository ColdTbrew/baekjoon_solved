from collections import deque

# 입력 받기
N, M = map(int, input().split())
campus = [list(input()) for _ in range(N)]

# 도연이의 시작 위치 찾기
start = None
for i in range(N):
    for j in range(M):
        if campus[i][j] == 'I':
            start = (i, j)
            break
    if start:
        break

# BFS로 탐색
def bfs(start_x, start_y):
    visited = [[False] * M for _ in range(N)]
    queue = deque([(start_x, start_y)])
    visited[start_x][start_y] = True
    people = 0  # 만난 사람 수
    
    # 상하좌우 이동 방향
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    while queue:
        x, y = queue.popleft()
        # 사람 만나면 카운트
        if campus[x][y] == 'P':
            people += 1
        
        # 상하좌우 탐색
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            # 범위 내이고, 벽이 아니고, 방문하지 않았으면 이동
            if 0 <= nx < N and 0 <= ny < M and campus[nx][ny] != 'X' and not visited[nx][ny]:
                visited[nx][ny] = True
                queue.append((nx, ny))
    
    return people

# 결과 계산 및 출력
result = bfs(start[0], start[1])
print(result if result > 0 else "TT")