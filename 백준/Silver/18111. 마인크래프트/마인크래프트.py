import sys
input = sys.stdin.readline

N, M, B = map(int, input().split())

ground = [list(map(int, input().split())) for _ in range(N)]

min_h = min(min(row) for row in ground)
max_h = max(max(row) for row in ground)

min_time = float('inf')
best_H = 0
for H in range(min_h, max_h+1):
    time = 0
    inventory = B
    for i in range(N):
        for j in range(M):
            diff = ground[i][j] - H
            if diff > 0:
                # 높이가 더 높음 -> 제거
                time += diff * 2
                inventory += diff
            elif diff < 0:
                time += -diff
                inventory += diff
    if inventory >= 0:
        if time <= min_time:
            min_time = time
            best_H = H
        elif time == min_time:
            best_height = max(best_height, H)
print(min_time, best_H)