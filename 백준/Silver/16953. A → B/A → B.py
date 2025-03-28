import sys
input = sys.stdin.readline

A, B = map(int, input().split())

from collections import deque
visited = set()
q = deque()
q.append((A, 0))
visited.add(A)

while q:
    cur, count = q.popleft()
    if cur == B:
        print(count+1)
        break
    next_node = cur*2
    if next_node <= B and next_node not in visited:
        visited.add(next_node)
        q.append((next_node, count+1))    
    next_node = cur*10+1
    if next_node <= B and next_node not in visited:
        visited.add(next_node)
        q.append((next_node, count+1))

else:
    print(-1)