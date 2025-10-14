# 레벨이 낮을 수록 얻는 점수가 작아야함
# 그리디 하게 그때의 선택의 최선의 선택이 되도록 선택하면됨
n = int(input())
scores = [int(input()) for _ in range(n)]
# print(scores)

# 뒤에서 부터 나보다 작지 않으면 나보다 작아지질때 까지 감소시킴
answer = 0

for i in range(n-1, 0, -1):
    while scores[i] <= scores[i-1]:
        scores[i-1] -= 1
        answer += 1
    # print(scores)
print(answer)
