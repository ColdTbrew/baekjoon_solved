# 입력
N, tae, P = map(int, input().split())
if N > 0:
    l = list(map(int, input().split()))
else:
    l = []

# 랭킹 리스트가 비어있는 경우
if N == 0:
    print(1)  # 태수의 점수는 1등
    exit()

# 랭킹 계산
rank = 1
for i in range(N):
    if tae < l[i]:  # 태수의 점수가 현재 점수보다 작으면
        rank += 1   # 등수는 증가
    elif tae == l[i]:  # 태수의 점수가 현재 점수와 같으면
        break  # 같은 점수의 등수를 유지
    else:  # 태수의 점수가 현재 점수보다 크면
        break  # 현재 등수 확정

# 리스트가 꽉 차있고, 태수의 점수가 마지막 점수보다 작거나 같으면
if N == P and tae <= l[-1]:
    print(-1)  # 랭킹에 오를 수 없음
else:
    print(rank)  # 계산된 등수 출력