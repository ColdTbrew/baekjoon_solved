N = int(input())
buildings = [int(input()) for _ in range(N)]

stack = [] # 스택에는 빌딩의 높이만 저장
total_count = 0

for h in buildings:
    while stack and h >= stack[-1]:
        stack.pop()

    total_count += len(stack)

    stack.append(h)

print(total_count)