import sys
input = sys.stdin.readline

N, M = map(int, input().split())
grid = []
for i in range(N):
    l = list(input().strip())
    grid.append([int(i) for i in l ])
    
ans = [[0]* M for _ in range(N)]


# 각 벽인 위치를 벽들 리스트에 담아두고 
# 하나의 벽식 부셔가면서 BFS로 도달가능한 노드 개수 새기
walls = []
for i in range(N):
    for j in range(M):
        if grid[i][j] == 1:
            walls.append((i, j))

from collections import deque
group_id = [[-1] * M for _ in range(N)]  # 각 칸의 그룹 ID
group_size = {}  # 그룹 ID -> 크기
group_cnt = 0  # 그룹 ID 카운터

dxs, dys = [0, 0, -1, 1], [-1, 1, 0, 0]

def bfs(i, j, gid): #그룹에서 인접한 0의 개수 
    q = deque()
    q.append((i, j))
    group_id[i][j] = gid
    count = 1
    while q:
        curi, curj = q.popleft()
        for dx, dy in zip(dxs, dys):
            nx, ny = curi+dx, curj + dy
            if 0<=nx<N and 0<=ny <M and grid[nx][ny] == 0 and group_id[nx][ny] == -1:
                group_id[nx][ny] = gid
                q.append((nx, ny))
                count += 1
    return count

# 0인 칸들 그룹화
for i in range(N):
    for j in range(M):
        if grid[i][j] == 0 and group_id[i][j] == -1:
            group_size[group_cnt] = bfs(i, j, group_cnt)
            group_cnt += 1

for i in range(N):
    for j in range(M):
        if grid[i][j] == 1:
            adj_groups = set()
            for dx, dy in zip(dxs, dys):
                ni, nj = i+dx, j + dy
                if 0<=ni<N and 0<=nj<M and grid[ni][nj] == 0:
                    adj_groups.add(group_id[ni][nj])
            ans[i][j] = (1+ sum(group_size[gid] for gid in adj_groups)) % 10

for row in ans:
    print(''.join(map(str, row)))