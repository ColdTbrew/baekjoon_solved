import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())
ladders = {}
snakes = {}
board = [(0,float('inf'))]* 101
for _ in range(N):
    x, y = map(int, input().split())
    # ladders[x] = y, 0 
    board[x] = (y, float('inf'))
for _ in range(M):
    x, y = map(int, input().split())
    # snakes[x] = y
    board[x] = (y, float('inf'))
# bfs로 해야함
# print(board)


def bfs(start):
    visited= [False] * 101
    visited[start] = True
    q = deque()
    q.append((start, 0))
    while q:
        cur, dist = q.popleft()
        if cur == 100:
            return dist
        for i in range(1, 7):
            new = cur + i
            new_dist = dist + 1
            # print("new",new)
            if 0<new< 101 and not visited[new]:
                if board[new][0] != 0: #다음으로 가는곳이 적힌놈
                    visited[board[new][0]] = True    
                    q.append((board[new][0], new_dist))
                else:
                    visited[new] = True
                    q.append((new, new_dist))
                if board[new][1] > new_dist:
                    board[new] = (board[new][0], new_dist)

print(bfs(1))
# print(board[100])