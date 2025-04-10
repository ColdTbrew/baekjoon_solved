import sys
from collections import deque
input = sys.stdin.readline

gears = [deque(map(int, input().strip())) for _ in range(4)]
# print(gears)
K = int(input().strip())

def is_different(gear1, gear2):
    return gears[gear1][2] != gears[gear2][6] #다르면 참

def rotate(gear_idx, d):
    if d == 1: #시계방향
        last = gears[gear_idx].pop()
        gears[gear_idx].appendleft(last)
    elif d == -1: #반시계방향
        last = gears[gear_idx].popleft()
        gears[gear_idx].append(last)
    
def check_rotate(connections, need, idx, direction):
    if 0>idx or idx>3:
        return
    if (idx, direction) in need:
        return
    need.append((idx, direction))
    if idx > 0 and connections[idx - 1] == 1:
        check_rotate(connections, need, idx - 1, -direction)
    if idx < 3 and connections[idx] == 1:
        check_rotate(connections, need, idx + 1, -direction)
    
connections = [0] * 3
for _ in range(K):
    gear_num, direction = map(int, input().split())

    for i in range(3):
        if is_different(i, i+1):
            connections[i] = 1
        else:
            connections[i] = 0
    # print(connections)
    need_to_rotate = []
    check_rotate(connections, need_to_rotate, gear_num-1, direction)
    # print("need_to_rotate", need_to_rotate)
    # print("-------------")

    for idx, d in need_to_rotate:
        rotate(idx, d)

score = 0
for i in range(4):
    if gears[i][0] == 1: score += 2 ** i

print(score)