N = int(input())
stalls = []
for _ in range(N):
    L, H = map(int, input().split())
    stalls.append((L, H))

stalls.sort()

# 가장 높은 기둥의 높이와 인덱스를 찾기
max_h = 0
max_h_idx = 0
for i, (l, h) in enumerate(stalls):
    if h > max_h:
        max_h = h
        max_h_idx = i

total_area = 0
current_max_h = 0

for i in range(max_h_idx):

    current_max_h = max(current_max_h, stalls[i][1])
    total_area += current_max_h * (stalls[i+1][0] - stalls[i][0])

current_max_h = 0


for i in range(N - 1, max_h_idx, -1):
    current_max_h = max(current_max_h, stalls[i][1])
    total_area += current_max_h * (stalls[i][0] - stalls[i-1][0])

total_area += max_h

print(total_area)