N, M, L, K = map(int, input().split())

stars = []
x_candidates = set()
y_candidates = set()

for _ in range(K):
    x, y = map(int, input().split())
    stars.append((x, y))
    x_candidates.add(x)
    y_candidates.add(y)

max_count = 0
# 모든 후보 x, y 좌표에 대해 반복
for start_x in x_candidates:
    for start_y in y_candidates:
        count = 0
        # 각 별이 현재 정사각형 내에 있는지 확인
        for star_x, star_y in stars:
            if start_x <= star_x <= start_x + L and start_y <= star_y <= start_y + L:
                count += 1
        max_count = max(max_count, count)
print(K-max_count)