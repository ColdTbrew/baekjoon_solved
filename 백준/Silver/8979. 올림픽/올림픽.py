import sys
input = sys.stdin.readline

N, K = map(int, input().split())

target_score = []
scores = []
for _ in range(N):
    # k 번째인 점수를 저장해두었다가
    # 정렬을 시킨다음에 찾아가자
    row = list(map(int, input().split()))
    k , score = row[0] , row[1:]
    if k == K:
        target_score = score
    scores.append(score)

scores.sort(key = lambda x : (x[0],x[1],x[2]), reverse=True)
# print(target_score)
# print(scores)
top = 1
for s in scores:
    if not s == target_score:
        top += 1
    else:
        break
print(top)
