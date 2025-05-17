import sys
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [list(input().strip()) for _ in range(N)]

group_id = 1
visited = [[0] * M for _ in range(N)]

directions = {
    'D' : (1, 0),
    'U' : (-1, 0),
    'L' : (0, -1),
    'R' : (0, 1)
}
def dfs(i, j):
    global group_id
    visited[i][j] = 1 # 방문 중

    dx, dy = directions[graph[i][j]]
    ni, nj = i+dx, j+dy

    if visited[ni][nj] == 0: # 방문한적 없는 곳이면 재귀 호출
        dfs(ni, nj)
    elif visited[ni][nj] == 1: # 방문 중인 곳이 dfs에 탐지되면 사이클이 발생한 것이기 때문에 새 그룹 생성
        group_id += 1 # 새 그룹 생성
    visited[i][j] = 2 # 이미 완료된곳을 표싷함

for i in range(N):
    for j in range(M):
        dfs(i, j)
        
print(group_id-1)