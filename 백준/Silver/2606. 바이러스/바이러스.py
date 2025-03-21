import sys
input = sys.stdin.readline

N = int(input().strip())
connections = int(input().strip())

# 연결리스트로 구현할거임
links = [[] for _ in range(N+1)]
for i in range(connections):
    start, end = map(int, input().split())
    links[start].append(end)
    links[end].append(start)
# 1 번 컴퓨터랑 이어진 연결된 컴퓨터들
infected = set()

def dfs(start):
    # if start in infected:
    #     return
    infected.add(start)
    for neighboor in links[start]:
        if neighboor not in infected:
            # print(neighboor)
            infected.add(neighboor)
            dfs(neighboor)
dfs(1)
# print("infected", infected)
print(len(infected)-1)
