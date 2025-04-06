from collections import deque

# 입력
M, N, H = map(int, input().split())
box = [[[] for _ in range(N)] for _ in range(H)]
for h in range(H):
    for i in range(N):
        row = list(map(int, input().split()))
        box[h][i] = row

# 6방향
dxs, dys, dzs = [0, 0, -1, 1, 0, 0], [1, -1, 0, 0, 0, 0], [0, 0, 0, 0, 1, -1]

def is_safe(z, x, y):
    return 0 <= z < H and 0 <= x < N and 0 <= y < M

def bfs():
    visited = [[[False] * M for _ in range(N)] for _ in range(H)]
    dist = [[[0] * M for _ in range(N)] for _ in range(H)]
    q = deque()
    
    # 모든 익은 토마토를 큐에 추가
    for z in range(H):
        for x in range(N):
            for y in range(M):
                if box[z][x][y] == 1:
                    visited[z][x][y] = True
                    q.append((z, x, y))
    
    # BFS
    while q:
        z, x, y = q.popleft()
        for dz, dx, dy in zip(dzs, dxs, dys):
            nz, nx, ny = z + dz, x + dx, y + dy
            if (is_safe(nz, nx, ny) and not visited[nz][nx][ny] and 
                box[nz][nx][ny] == 0):  # 0만 익히기
                visited[nz][nx][ny] = True
                box[nz][nx][ny] = 1
                dist[nz][nx][ny] = dist[z][x][y] + 1
                q.append((nz, nx, ny))
    
    # 다 익었는지 확인 및 최대 거리 계산
    max_dist = 0
    for z in range(H):
        for x in range(N):
            for y in range(M):
                if box[z][x][y] == 0:  # 익지 않은 토마토 남음
                    return -1
                if box[z][x][y] == 1:  # 모든 1의 거리 체크
                    max_dist = max(max_dist, dist[z][x][y])
    return max_dist

# 처음부터 다 익었는지 확인
all_ripe = True
for z in range(H):
    for x in range(N):
        for y in range(M):
            if box[z][x][y] == 0:
                all_ripe = False
                break
        if not all_ripe:
            break
    if not all_ripe:
        break

if all_ripe:
    print(0)
else:
    print(bfs())