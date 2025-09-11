N = int(input())
K = int(input())
sensors = list(map(int, input().split()))
sensors.sort()
if K >= N:
    print(0)
    exit()
dist = []
for s_idx in range(1, N):
    dist.append(sensors[s_idx] - sensors[s_idx-1])

dist.sort(reverse=False)
# print(sensors)
# print(dist)
min_sum = float('inf')

for k in range(K-1):
    dist.pop()
    # min_sum = min(min_sum, sum(dist))
# print(dist)
print(sum(dist))