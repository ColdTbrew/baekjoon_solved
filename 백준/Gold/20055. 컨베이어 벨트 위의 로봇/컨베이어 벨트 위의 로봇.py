import sys
from collections import deque

def solve():
    N, K = map(int, sys.stdin.readline().split())
    belt = deque(map(int, sys.stdin.readline().split()))
    
    # 로봇이 있는 위치를 True/False로 표시하는 덱. N개의 칸만 필요함 (올리는 위치부터 내리는 위치까지)
    robots = deque([False] * N)
    
    step_count = 0
    while True:
        step_count += 1
        
        belt.rotate(1)
        robots.rotate(1)
        
        robots[N-1] = False
    

        for i in range(N - 2, -1, -1):
            if robots[i]:
                if not robots[i+1] and belt[i+1] >= 1:
                    robots[i+1] = True
                    robots[i] = False
                    belt[i+1] -= 1    
        

        robots[N-1] = False

    
        if belt[0] >= 1 and not robots[0]:
            robots[0] = True
            belt[0] -= 1

    
        zero_count = 0
        for durability in belt:
            if durability == 0:
                zero_count += 1
        
        if zero_count >= K:
            print(step_count)
            break

solve()