from collections import deque
from itertools import combinations
from copy import deepcopy

def get_dist(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)

def step_down(temp_grid):
    temp_grid.pop()              # 맨 아래 행 제거 (성 쪽으로 내려가서 사라짐)
    temp_grid.appendleft([0]*M)  # 맨 위에 빈 행 추가 (새 공간)
    
def enemy_can_see(enemys, archer_pos):
    can_see = []
    for ex, ey in enemys:
        dist = get_dist(archer_pos[0], archer_pos[1], ex, ey)
        if dist <= D:
            can_see.append((ex, ey, dist))
    # 거리 -> 열(왼쪽 우선) 순서
    return sorted(can_see, key=lambda x: (x[2], x[1]))

def get_enemys(grid):
    enemys = []
    for i in range(N):
        for j in range(M):
            if grid[i][j] == 1:
                enemys.append((i, j))
    return enemys

N, M, D = map(int, input().split())
grid = deque()
for _ in range(N):
    grid.append(list(map(int, input().split())))

max_enemy = 0

for selected in combinations(range(M), 3):  # 궁수 위치 3개 조합
    killed = 0
    temp_grid = deepcopy(grid)
    archers = [(N, c) for c in selected]

    # 최대 N턴 진행 (적이 모두 내려오거나 없어질 때까지)
    for _ in range(N):
        enemys = get_enemys(temp_grid)
        if not enemys:
            break

        targets = set()
        for archer_pos in archers:
            can_see = enemy_can_see(enemys, archer_pos)
            if can_see:
                tx, ty, _ = can_see[0]
                targets.add((tx, ty))

        # 타겟 적 제거
        for tx, ty in targets:
            if temp_grid[tx][ty] == 1:
                temp_grid[tx][ty] = 0
                killed += 1

        # 적 한 칸 아래로 이동
        step_down(temp_grid)

    max_enemy = max(max_enemy, killed)

print(max_enemy)