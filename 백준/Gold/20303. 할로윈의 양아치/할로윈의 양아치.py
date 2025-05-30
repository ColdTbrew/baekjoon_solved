import sys
input = sys.stdin.readline

# 입력 받기
N, M, K = map(int, input().split())
candies = [0] + list(map(int, input().split()))  # 1-based indexing을 위해 0번 인덱스에 0 추가

# 그래프 생성 (인접 리스트)
graph = [[] for _ in range(N + 1)]
for _ in range(M):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

# DFS로 연결된 그룹 찾기
def dfs(start, visited):
    stack = [start]
    visited[start] = True
    group_size = 1  # 그룹에 속한 아이 수
    group_candies = candies[start]  # 그룹의 사탕 합계
    while stack:
        node = stack.pop()
        for neighbor in graph[node]:
            if not visited[neighbor]:
                visited[neighbor] = True
                stack.append(neighbor)
                group_size += 1
                group_candies += candies[neighbor]
    return group_size, group_candies

# 친구 그룹 찾기
visited = [False] * (N + 1)
groups = []  # (그룹의 아이 수, 그룹의 사탕 합계) 리스트
for i in range(1, N + 1):
    if not visited[i]:
        size, candy_sum = dfs(i, visited)
        groups.append((size, candy_sum))

group_count = len(groups)
dp = [[0] * K for _ in range(group_count + 1)]  # dp[i][j]: i번째 그룹까지 고려, j명 선택 시 최대 사탕

for i in range(1, group_count + 1):
    size, candy = groups[i - 1]  # i번째 그룹의 아이 수와 사탕 합계
    for j in range(K):
        # 그룹을 선택하지 않는 경우
        dp[i][j] = dp[i - 1][j]
        # 그룹을 선택하는 경우 (j >= size일 때만 가능)
        if j >= size:
            dp[i][j] = max(dp[i][j], dp[i - 1][j - size] + candy)

# K 미만의 아이를 선택했을 때 최대 사탕 수 구하기
result = max(dp[group_count][j] for j in range(K))
print(result)