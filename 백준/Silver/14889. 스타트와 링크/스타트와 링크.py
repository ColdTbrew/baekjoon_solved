import sys
from collections import deque
from itertools import combinations
from itertools import permutations
input = sys.stdin.readline

N = int(input().strip())
benefit = [list(map(int, input().split())) for _ in range(N)]

persons = range(1, N+1)

min_diff = float('inf')
for team1 in combinations(persons, N//2):
    # print(team1)
    team2 = []
    for p in persons:
        if p not in set(team1):
            team2.append(p)
    # print(team2)

    team1_score = 0
    team2_score = 0
    for team in combinations(team1, 2):
        i,j  = team[0],team[1]
        team1_score += benefit[i-1][j-1] + benefit[j-1][i-1]
    for team in combinations(team2, 2):
        i,j  = team[0],team[1]
        team2_score += benefit[i-1][j-1] + benefit[j-1][i-1]
    diff = abs(team1_score - team2_score)
    min_diff = min(diff, min_diff)

print(min_diff)