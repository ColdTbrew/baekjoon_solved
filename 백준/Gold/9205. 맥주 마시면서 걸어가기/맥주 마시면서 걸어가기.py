import sys
input = sys.stdin.readline
T = int(input())
bear_left = 20

def dist(x, y, i, j):
    return abs(x-i) + abs(y-j)

from collections import deque
for i in range(T):
    is_happy = False
    num_gs25 = int(input())
    
    start_x, start_y = map(int, input().split())
    points = []
    points.append((start_x, start_y))
    for j in range(num_gs25):
        x, y = map(int, input().split())
        points.append((x, y))
    end_x, end_y = map(int, input().split())
    points.append((end_x, end_y))
    
    queue = deque([0])
    visited = [False] * (num_gs25+2)
    visited[0] = True
    
    while queue:
        current = queue.popleft()
        if current == num_gs25+1:
            is_happy = True
            break
        for next_node in range(num_gs25+2):
            if not visited[next_node]:
                if dist(points[current][0], points[current][1], points[next_node][0], points[next_node][1] ) <= 1000:
                    visited[next_node] = True
                    queue.append(next_node)
    print("happy" if is_happy else "sad")