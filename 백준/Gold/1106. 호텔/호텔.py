import sys
input = sys.stdin.readline

C, N = map(int, input().split())
cities = []
for i in range(N):
    cost, person = map(int, input().split())
    cities.append((cost, person))

INF = float('inf')
max_person = max(person for _, person in cities)

dp = [INF] * (C + max_person + 1)
dp[0] = 0
# dp i 는 사람이 i일때의 최소 비용

for j in range(C+ max_person + 1): # 적어도 C명 늘려야함 그래서 dp[C+max_person] 즉 C+max_person일때의 최소비용
    for cost, person in cities:
        if j >= person:
            dp[j] = min(dp[j], dp[j-person] + cost)

result = min(dp[C:C+max_person+1])
print(result)