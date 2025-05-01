import sys
input = sys.stdin.readline
N, M = map(int, input().split())

dependency = [[] for _ in range(N+1)]
indegree = [0 for _ in range(N+1)]
for _ in range(M):
    row = list(map(int, input().split()))
    count = row[0]
    # 위상 정렬 사용해야하고
    # 의존 리스트 
    # indegree 리스트
    for i in range(1, len(row)-1):
        dependency[row[i]].append(row[i+1])
        indegree[row[i+1]] += 1
    

# print("dependency", dependency)
# print("indegree", indegree)

from collections import deque
q = deque()
for i in range(1, N+1):
    if indegree[i] == 0:
        q.append(i)

ans = []
while q:
    cur = q.popleft()
    ans.append(cur)
    for next in dependency[cur]:
        indegree[next] -= 1
        if indegree[next] == 0:
            q.append(next)

# 불가능한경우 체크하기

if len(ans) != N:
    print(0)
else:
    print(*ans,sep = "\n")

"""
6 3
3 1 3 4
4 6 2 5 4 
3 2 3 1
"""