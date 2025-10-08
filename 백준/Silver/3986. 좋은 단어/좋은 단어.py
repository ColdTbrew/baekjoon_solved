ans = 0
T = int(input())
for _ in range(T):
    A = list(input().strip())
    stack = []
    for a in A:
        if stack and stack[-1] == a:
            stack.pop()
        else:
            stack.append(a)
    if not stack:
        ans += 1
print(ans)