N, M = map(int, input().split())
cources = []
need_ma = []
for _ in range(N):
    p, l = map(int, input().split())
    # 신청한 사람수 , 수강인원
    applied = list(map(int, input().split()))
    # 신청한 마일리지를 정렬후에 수강인원만큼 남긴다 했을때 그때의 제일 작은수보다 + 1인걸 저장
    applied.sort(reverse=True)
    applied = applied[:l]
    # print("커트 라인", applied)
    min_ma = applied[-1]
    # print("min_ma + 1", min_ma)
    if p < l:
        need_ma.append(1)
    else:
        need_ma.append(min_ma)

cnt = 0
need_ma.sort()
for n in need_ma:
    if n <= M:
        cnt += 1
        M -= n
# print(need_ma)
print(cnt)