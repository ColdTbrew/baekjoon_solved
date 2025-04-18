import sys
input = sys.stdin.readline

def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, a, b):
    a = find(parent, a)
    b = find(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

# 입력
N, M = map(int, input().split())
truth = list(map(int, input().split()))[1:]  # 진실 아는 사람
parties = [list(map(int, input().split()))[1:] for _ in range(M)]

# 유니온-파인드 초기화
parent = list(range(N + M + 1))  # 1~N: 사람, N+1~N+M: 파티

# 각 파티와 참석자 연결
for i in range(M):
    party = parties[i]
    party_node = N + 1 + i  # 파티 노드: N+1부터
    for person in party:
        union(parent, person, party_node)

# 진실 아는 사람과 연결된 파티 확인
truth_set = set()
for person in truth:
    truth_set.add(find(parent, person))

# 과장 가능한 파티 수 계산
ans = 0
for i in range(M):
    party_node = N + 1 + i
    if find(parent, party_node) not in truth_set:
        ans += 1

print(ans)