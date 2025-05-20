import sys
from collections import deque

input = sys.stdin.readline

T = int(input())
dxs, dys = [0, 0, -1, 1], [-1, 1, 0, 0]

def bfs(h, w, graph, has_keys):
    visited = [[False] * w for _ in range(h)]
    q = deque()
    doors = {chr(i): [] for i in range(ord('A'), ord('Z')+1)}
    docs = 0

    # 테두리에서 시작 가능한 지점 큐에 추가
    for i in range(h):
        for j in range(w):
            if (i == 0 or i == h-1 or j == 0 or j == w-1) and graph[i][j] != '*':
                q.append((i, j))
                visited[i][j] = True

    while q:
        x, y = q.popleft()
        cur = graph[x][y]

        if 'A' <= cur <= 'Z':
            if cur.lower() not in has_keys:
                doors[cur].append((x, y))
                continue  # 열쇠 없으면 대기
        elif 'a' <= cur <= 'z':
            if cur not in has_keys:
                has_keys.add(cur)
                # 이전에 못 갔던 문들 다시 큐에 추가
                for door_x, door_y in doors[cur.upper()]:
                    q.append((door_x, door_y))
                doors[cur.upper()] = []

        elif cur == '$':
            docs += 1
            graph[x][y] = '.'  # 문서 회수 처리

        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            if 0 <= nx < h and 0 <= ny < w and not visited[nx][ny] and graph[nx][ny] != '*':
                visited[nx][ny] = True
                q.append((nx, ny))

    return docs

for _ in range(T):
    h, w = map(int, input().split())
    graph = [list(input().strip()) for _ in range(h)]
    key_input = input().strip()
    has_keys = set(key_input) if key_input != '0' else set()

    print(bfs(h, w, graph, has_keys))
