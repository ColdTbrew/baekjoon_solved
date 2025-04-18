import sys
from collections import deque

input = sys.stdin.readline

def double(num):
    return (2 * num) % 10000

def sub(num):
    return (num - 1) % 10000

def left(num):
    return (num % 1000) * 10 + num // 1000

def right(num):
    return (num % 10) * 1000 + num // 10

def bfs(start, end):
    visited = [False] * 10000
    parent = [(-1, '') for _ in range(10000)]
    q = deque([start])
    visited[start] = True
    ops = ['D', 'S', 'L', 'R']
    
    while q:
        cur = q.popleft()
        if cur == end:
            ans = []
            while parent[cur][0] != -1:
                ans.append(parent[cur][1])
                cur = parent[cur][0]
            return ans[::-1]
        
        for op in ops:
            if op == 'D':
                new = double(cur)
            elif op == 'S':
                new = sub(cur)
            elif op == 'L':
                new = left(cur)
            else:  # op == 'R'
                new = right(cur)
                
            if 0 <= new < 10000 and not visited[new]:
                visited[new] = True
                parent[new] = (cur, op)
                q.append(new)

T = int(input().strip())
for _ in range(T):
    A, B = map(int, input().split())
    print(''.join(bfs(A, B)))