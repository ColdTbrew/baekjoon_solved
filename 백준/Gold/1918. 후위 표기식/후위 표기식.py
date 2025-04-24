import sys
input = sys.stdin.readline

inorder = input().strip()

ans = []
stack = []
priority = {'+':1, '-':1, '*':2, '/':2, '(':0}
for c in inorder:
    if 'A'<= c <='Z':
        ans.append(c)
    elif c == ')':
        while stack and stack[-1] != '(':
            ans.append(stack.pop())
        stack.pop()
    elif c == '(':
        stack.append(c)
    else:
        while stack and priority[stack[-1]] >= priority[c]:
            pop = stack.pop()
            if pop != '(':
                ans.append(pop)
        stack.append(c)
    # print("cur stack", *stack)
    # print("cur ans ", *ans)
if stack:
    while stack:
        top = stack.pop()
        if top != '(':
            ans.append(top)

print(*ans, sep='')