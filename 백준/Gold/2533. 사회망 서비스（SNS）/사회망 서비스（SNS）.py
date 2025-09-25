N = int(input())
tree = [[] for _ in range(N+1)]
for _ in range(N-1):
    p, c = map(int, input().split())
    tree[p].append(c)
    tree[c].append(p)

dp = [[0, 0] for _ in range(N+1)]

def iterative_dfs(root):
    stack = [(root, 0, False)]  # (노드, 부모, 방문 완료 여부)
    while stack:
        v, parent, done = stack.pop()
        if done:  # 자식 처리가 완료된 경우
            dp[v][0] = 0
            dp[v][1] = 1
            for u in tree[v]:
                if u != parent:
                    dp[v][0] += dp[u][1]
                    dp[v][1] += min(dp[u][0], dp[u][1])
        else:  # 자식들을 먼저 탐색
            stack.append((v, parent, True))  # 현재 노드를 나중에 처리
            for u in tree[v]:
                if u != parent:
                    stack.append((u, v, False))  # 자식을 스택에 추가

iterative_dfs(1)
print(min(dp[1][0], dp[1][1]))