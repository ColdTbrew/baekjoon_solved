import sys
from collections import deque

input = sys.stdin.readline

grid = []
for _ in range(12):
    grid.append(list(input().strip()))

dxs = [0, 0, -1, 1]
dys = [-1, 1, 0, 0]

# 현재 grid에서 터질 블록들을 찾아 리스트로 반환
def find_exploding_blocks():
    exploding_blocks = set()
    visited = [[False for _ in range(6)] for _ in range(12)]

    for i in range(12):
        for j in range(6):
            if grid[i][j] != '.' and not visited[i][j]:
                color = grid[i][j]
                
                # BFS를 위한 큐와 임시 방문 리스트
                q = deque([(i, j)])
                temp_visited = [(i, j)]
                visited[i][j] = True
                
                while q:
                    x, y = q.popleft()
                    
                    for dx, dy in zip(dxs, dys):
                        nx, ny = x + dx, y + dy
                        
                        if 0 <= nx < 12 and 0 <= ny < 6 and not visited[nx][ny] and grid[nx][ny] == color:
                            visited[nx][ny] = True
                            q.append((nx, ny))
                            temp_visited.append((nx, ny))
                
                if len(temp_visited) >= 4:
                    for block in temp_visited:
                        exploding_blocks.add(block)
                        
    return exploding_blocks

def boom(exploding_blocks):
    if not exploding_blocks:
        return False
        
    for i, j in exploding_blocks:
        grid[i][j] = '.'
    return True

def drop():
    for j in range(6):
        void_cnt = 0
        for i in range(11, -1, -1):
            if grid[i][j] == '.':
                void_cnt += 1
            elif void_cnt > 0:
                grid[i + void_cnt][j] = grid[i][j]
                grid[i][j] = '.'

combo = 0
while True:
    exploding_blocks = find_exploding_blocks()
    
    if not boom(exploding_blocks):
        break
    
    drop()
    combo += 1

print(combo)