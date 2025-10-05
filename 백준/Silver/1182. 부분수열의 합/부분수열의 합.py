N, S = map(int, input().split())
array = list(map(int, input().split()))

select = []
answer = 0

def bt(start, sum_acc):
    global answer, N  # N 명시 (안전성)
    if sum_acc == S and len(select) > 0:
        answer += 1
        # return 제거: 계속 탐색
    for i in range(start, N):
        select.append(array[i])
        bt(i + 1, sum_acc + array[i])
        select.pop()

bt(0, 0)
print(answer)