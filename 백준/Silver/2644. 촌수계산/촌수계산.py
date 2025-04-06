from collections import deque

N = int(input())
x, y = map(int, input().split())
m = int(input())

# 양방향 그래프
grid = [[] for _ in range(N+1)]
for _ in range(m):
    u, v = map(int, input().split())
    grid[u].append(v)
    grid[v].append(u)

# BFS로 촌수 계산
def bfs(start, target):
    visited = [False] * (N+1)
    queue = deque([(start, 0)])  # (노드, 촌수)
    visited[start] = True
    
    while queue:
        current, count = queue.popleft()
        if current == target:
            return count
        for neighbor in grid[current]:
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append((neighbor, count + 1))
    return -1

# 실행
result = bfs(x, y)
print(result)