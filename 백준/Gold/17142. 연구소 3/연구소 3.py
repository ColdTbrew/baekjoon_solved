import sys
from itertools import combinations
from collections import deque

input = sys.stdin.readline

# 입력
N, M = map(int, input().split())
grid = []
deactives = []
empty_count = 0  # 빈칸(0)의 개수
for i in range(N):
    row = list(map(int, input().split()))
    grid.append(row)
    for j, x in enumerate(row):
        if x == 2:
            deactives.append((i, j))
        elif x == 0:
            empty_count += 1

# 빈칸이 없는 경우
if empty_count == 0:
    print(0)
    sys.exit(0)

# BFS로 바이러스 퍼뜨리기
dxs, dys = [0, 0, -1, 1], [-1, 1, 0, 0]
def spread(actives, empty_count):
    times = [[-1] * N for _ in range(N)]  # -1로 초기화
    q = deque()
    filled = 0
    
    # 활성 바이러스 초기화
    for i, j in actives:
        times[i][j] = 0
        q.append((i, j, 0))
    
    while q:
        curi, curj, curtime = q.popleft()
        for dx, dy in zip(dxs, dys):
            nx, ny = curi + dx, curj + dy
            if 0 <= nx < N and 0 <= ny < N and times[nx][ny] == -1:
                if grid[nx][ny] in (0, 2):
                    times[nx][ny] = curtime + 1
                    q.append((nx, ny, curtime + 1))
                    if grid[nx][ny] == 0:
                        filled += 1
    
    if filled == empty_count:
        max_time = 0
        for i in range(N):
            for j in range(N):
                if grid[i][j] == 0:
                    max_time = max(max_time, times[i][j])
        return max_time
    return float('inf')

# 최소 시간 계산
min_time = float('inf')
for actives in combinations(deactives, M):
    result = spread(actives, empty_count)
    min_time = min(min_time, result)

# 결과 출력
print(min_time if min_time != float('inf') else -1)