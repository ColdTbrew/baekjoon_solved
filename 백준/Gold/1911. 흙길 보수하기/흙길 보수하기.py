#N개의 물웅덩이, 길이가L인 널빤지
N, L = map(int, input().split())
pits = []
for _ in range(N):
    pit_s, pit_e = map(int, input().split())
    pits.append((pit_s, pit_e))

pits.sort(key = lambda x: x[0])

cnt = 0
cur = 0
pit_idx = pits[0][0]
for p1, p2 in pits:
    if p1 > pit_idx:
        pit_idx = p1
    length = p2 - pit_idx
    if length % L == 0: #나누어 떨어지면
        cnt += length//L
        pit_idx = p2
    else:
        cnt += length//L + 1
        pit_idx = p2 + (L-length%L) # 꼬다리 추가


print(cnt)