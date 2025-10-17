import sys
input = sys.stdin.readline

N = int(input())
flowers = []
for _ in range(N):
    sm, sd, em, ed = map(int, input().split())
    s = sm * 100 + sd
    e = em * 100 + ed
    flowers.append((s, e))

flowers.sort()  # 시작일 기준

TARGET_START = 301
TARGET_END = 1201  # 12/01로 잡아야 11/30을 끝까지 덮을 수 있음

cur = TARGET_START
idx = 0
ans = 0
best = cur

while cur < TARGET_END:
    updated = False
    # cur 이하에서 시작하는 모든 구간 중 가장 멀리 가는 끝점을 고름
    while idx < N and flowers[idx][0] <= cur:
        if flowers[idx][1] > best:
            best = flowers[idx][1]
            updated = True
        idx += 1

    if not updated:  # 이어서 덮을 구간이 없음 → 불가능
        print(0)
        break

    ans += 1
    cur = best

if cur >= TARGET_END:
    print(ans)