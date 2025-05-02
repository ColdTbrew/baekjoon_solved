import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline

T = int(input())

def dfs(node, graph, visited, path):
    visited[node] = 1
    path.append(node)
    team_count = 0

    next_node = graph[node][0]
    if visited[next_node] == 1: # 다음 갈 곳이 방문했던 곳이면
        if next_node in path: # 경로에서 노드 개수 셈
            cycle_start = path.index(next_node)
            team_count = len(path) - cycle_start
    elif visited[next_node] == 0:
        team_count = dfs(next_node, graph, visited, path)
    visited[node] = 2
    path.pop()
    return team_count

for _ in range(T):
    n = int(input())
    array = list(map(int, input().split()))

    graph = [[] for _ in range(n+1)]
    for idx, num in enumerate(array, 1):  # 1-based 인덱스
        graph[idx].append(num)

    # print(graph)
    visited = [0] *(n+1)
    team_count = 0

    for i in range(1, n+1):
        if visited[i] == 0:
            team_count += dfs(i, graph, visited, [])
    print(n - team_count)

    # 주어진 선택의 결과를 보고 어느 프로젝트 팀에도 속하지 않는 학생들의 수를 계산하는 프로그램을 작성하라.
    