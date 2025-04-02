import sys
input = sys.stdin.readline


from itertools import combinations
N, M = map(int, input().split())

houses = []
chickens = []

for i in range(N):
    row = list(map(int, input().split()))
    for c_idx, r in enumerate(row):
        if r == 1:
            houses.append((i+1, c_idx+1))
        if r == 2:
            chickens.append((i+1, c_idx+1))

# print(houses)
# print(chickens)
# 치킨집을 len(chickens)에서 M개만 골라서 그때의 치킨 거리의 최소값 갱신
best_combi = float('inf')
for saved_chicken in combinations(chickens, M):
    # print(saved_chicken)
    road_len = 0
    for house in houses:
        temp_len = float('inf')
        for chicken in saved_chicken:
            temp = abs(house[0]-chicken[0]) + abs(house[1]-chicken[1])
            temp_len = min(temp_len, temp)
        road_len += temp_len
    best_combi = min(road_len, best_combi)
print(best_combi)