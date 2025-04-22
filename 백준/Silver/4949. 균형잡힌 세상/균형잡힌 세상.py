import sys
input = sys.stdin.readline

ans = []
while True:
    sentence = input().rstrip()  # 오른쪽 공백 및 개행 제거
    if sentence == '.':  # 종료 조건
        break
    
    # 온점 제거 (문자열 끝의 '.' 제외)
    if sentence.endswith('.'):
        sentence = sentence[:-1]
    
    stack = []
    is_balanced = True
    
    for char in sentence:
        if char == '(' or char == '[':
            stack.append(char)
        elif char == ')':
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                is_balanced = False
                break
        elif char == ']':
            if stack and stack[-1] == '[':
                stack.pop()
            else:
                is_balanced = False
                break
    
    # 균형 확인: is_balanced가 True이고 스택이 비어있어야 함
    if is_balanced and not stack:
        ans.append("yes")
    else:
        ans.append("no")

print(*ans, sep="\n")