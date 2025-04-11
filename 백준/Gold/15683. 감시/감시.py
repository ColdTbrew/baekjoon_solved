import sys
from collections import deque
from copy import deepcopy
from itertools import product
input = sys.stdin.readline

# CCTV 방향 패턴 (북, 동, 남, 서)
cctv = deque([deque([1, 0, 0, 0])])  # 1번
cctv.append(deque([0, 1, 0, 1]))     # 2번
cctv.append(deque([1, 1, 0, 0]))     # 3번
cctv.append(deque([1, 1, 0, 1]))     # 4번
cctv.append(deque([1, 1, 1, 1]))     # 5번

# 입력 처리
N, M = map(int, input().split())
office = [list(map(int, input().split())) for _ in range(N)]

def rotate(cctv, cctv_num):
    last = cctv[cctv_num].pop()
    cctv[cctv_num].appendleft(last)
    return cctv

def fill_office(office, direction, x, y):
    if direction == 0:  # 북
        while x >= 0:
            if office[x][y] == 6:
                break
            if office[x][y] == 0:
                office[x][y] = '#'
            x -= 1
    elif direction == 1:  # 동
        while y < M:
            if office[x][y] == 6:
                break
            if office[x][y] == 0:
                office[x][y] = '#'
            y += 1
    elif direction == 2:  # 남
        while x < N:
            if office[x][y] == 6:
                break
            if office[x][y] == 0:
                office[x][y] = '#'
            x += 1
    elif direction == 3:  # 서
        while y >= 0:
            if office[x][y] == 6:
                break
            if office[x][y] == 0:
                office[x][y] = '#'
            y -= 1
    return office

def can_see(office, cctv, cctv_num, x, y):
    for direction, active in enumerate(cctv[cctv_num]):
        if active == 1:
            office = fill_office(office, direction, x, y)
    return office

def count_blind_spot(office):
    count = 0
    for i in range(N):
        for j in range(M):
            if office[i][j] == 0:
                count += 1
    return count

def vis_office(office):
    for i in range(N):
        print(office[i])

# CCTV 위치 수집
cctvs = []
for i in range(N):
    for j in range(M):
        if 1 <= office[i][j] <= 5:
            cctvs.append((i, j))

# 모든 회전 조합 탐색
min_blind_spot = 64
for rotate_times in product(range(4), repeat=len(cctvs)):
    office_copy = deepcopy(office)
    cctv_copy = deepcopy(cctv)
    for idx, (x, y) in enumerate(cctvs):
        cctv_num = office[x][y] - 1
        for _ in range(rotate_times[idx]):
            cctv_copy = rotate(cctv_copy, cctv_num)
        office_copy = can_see(office_copy, cctv_copy, cctv_num, x, y)
    min_blind_spot = min(min_blind_spot, count_blind_spot(office_copy))

print(min_blind_spot)