import sys
input = sys.stdin.readline

T = int(input().strip())

for _ in range(T):
    N, M, K = map(int, input().split())
    maps = [[ 0 for _ in range(M)] for _ in range(N)]
    visited = [[ False for _ in range(M)] for _ in range(N)]
    # 지도 그리기
    for _ in range(K):
        i, j = map(int, input().split())
        maps[i][j] = 1
    # 탐색하기
    # 동서 남북 탐색하면서 visited 갱신 
    # 1인데 visited가 아니였으면 count += 1 섬 푸는 문제랑 동일
    from collections import deque
    dxs = [0, 0, -1, 1]
    dys = [1, -1, 0, 0]
    count = 0
    for i in range(N):
        for j in range(M):
            if not visited[i][j] and maps[i][j] == 1:
                q = deque()
                q.append((i, j))
                visited[i][j] = True
                count += 1
                while q:
                    x, y = q.popleft()   
                    for dx, dy in zip(dxs, dys):
                        newx, newy = x+dx, y+dy
                        if 0<=newy<M and 0<=newx<N and maps[newx][newy] == 1 and not visited[newx][newy]:
                            visited[newx][newy] = True
                            q.append((newx,newy))

    print(count)