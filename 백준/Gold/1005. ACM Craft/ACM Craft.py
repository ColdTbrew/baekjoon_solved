import sys
input = sys.stdin.readline
from collections import deque
T = int(input())
for _ in range(T):
    N, K = map(int, input().split())
    waiting = list(map(int, input().split()))
    dependency = [[] for _ in range(N+1)] # 후속 건물 리스트 담기
    indegree = [0 for _ in range(N+1)] # 선행건물의 수 , 위상정렬을 위해
    for _ in range(K):
        a, b = map(int, input().split())
        dependency[a].append(b)
        indegree[b] += 1

    dp = [0 for _ in range(N+1)] # 건물 i를 완성하는데 필요한 최소시간
    
    queue = deque()

    for i in range(1, N+1):
        if indegree[i] == 0:
            queue.append(i)
            dp[i] = waiting[i-1] # 선행 건물이 없는 놈을 큐에 넣고 시작하자
    while queue:
        cur = queue.popleft()
        for next in dependency[cur]:
            indegree[next] -= 1 # 선행건물 하나 소모
            dp[next] = max(dp[next], dp[cur] + waiting[next-1]) # next중에 최대시간을 골라 가져갈거임

            if indegree[next] == 0: # 선행 건물이 다 처리되면 큐에 넣겠다
                queue.append(next)
    
    
    
    W = int(input())
    print(dp[W])
"""
1
4 4
10 1 100 10
1 2
1 3
2 4
3 4
4
8 8
"""