n = int(input())

for _ in range(n):
    inputs = input()
    stack = []
    flag = "YES"  # 초기값

    for i in inputs:
        if i == "(":
            stack.append(i)
        elif i == ")":
            if stack and stack[-1] == "(":  # 스택이 있고 마지막이 '('면
                stack.pop()
            else:  # 스택이 비었거나 '('가 아니면
                flag = "NO"
                break  # 더 볼 필요 없음

    # 문자열 끝난 후 스택에 남은 '('가 있으면 NO
    if stack:
        flag = "NO"
    print(flag)


"""
6
(())())
(((()())()
(()())((()))
((()()(()))(((())))()
()()()()(()()())()
(()((())()(
"""