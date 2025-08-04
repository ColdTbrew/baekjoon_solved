N = int(input())
builds = list(map(int, input().split()))

ans = [0] * N
stack = [] # 높이, 인덱스 사용
# 스택은 이전 빌딩의 높은 놈 기록
for i in range(N):
    while stack and stack[-1][0] < builds[i]:
        stack.pop()
    if stack:
        ans[i] = stack[-1][1] + 1

    stack.append((builds[i], i))
    # print(stack)
print(*ans)