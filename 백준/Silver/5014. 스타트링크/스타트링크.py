from collections import deque


F, S, G, U, D = map(int, input().split())

# bfs를 통해서 오르고 내리고를 해서 버튼 수 계산
visited = [False] * (F+1)
dist = [0] *(F+1)
q = deque()
q.append(S)
visited[S] = True
while q:
    cur = q.popleft()
    if cur == G:  # 목표 층에 도달하면 종료
        break
    go_up = cur+U
    go_down = cur - D
    if go_up <= F and not visited[go_up]:
        visited[go_up] = True
        dist[go_up] = dist[cur] + 1
        q.append(go_up)
    if go_down > 0 and not visited[go_down]:
        visited[go_down] = True
        dist[go_down] = dist[cur] + 1
        q.append(go_down)

if visited[G]:
    print(dist[G])
else:
    print("use the stairs")