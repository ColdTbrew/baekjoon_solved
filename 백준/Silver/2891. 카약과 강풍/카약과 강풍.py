N, S, R = map(int, input().split())
damaged = list(map(int, input().split()))
spares = list(map(int, input().split()))

# set으로 변환하여 중복 처리
damaged_set = set(damaged)
spares_set = set(spares)
common = damaged_set & spares_set  # 중복 팀: 자신의 여분으로 수리
damaged_set -= common
spares_set -= common

ans = 0
damaged = sorted(list(damaged_set))  # 정렬하여 투 포인터 적용
spares = sorted(list(spares_set))
j = 0
for i in range(len(damaged)):
    d = damaged[i]
    matched = False
    # spares[j]가 d-1 이전이면 j 이동
    while j < len(spares) and spares[j] < d - 1:
        j += 1
    # 매칭 시도: d, d-1, d+1 우선순위
    if j < len(spares) and spares[j] == d:
        j += 1
        matched = True
    elif j < len(spares) and spares[j] == d - 1:
        j += 1
        matched = True
    elif j + 1 < len(spares) and spares[j + 1] == d + 1:
        j += 2  # d+1 매칭 시 j+1 건너뜀
        matched = True
    elif j < len(spares) and spares[j] == d + 1:
        j += 1
        matched = True
    if not matched:
        ans += 1

print(ans)