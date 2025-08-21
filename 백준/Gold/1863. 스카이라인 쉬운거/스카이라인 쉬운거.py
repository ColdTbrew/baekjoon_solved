N = int(input())

stack = []
b_cnt = 0
for _ in range(N):
    x, y = map(int, input().split())
    while stack and stack[-1] > y: # 스택에 현재 y 보다 큰 값이 있으면 높이가 달라진거니까 
        stack.pop()
        b_cnt += 1 # 빌딩카운트
    if stack and stack[-1] == y: # 이미 같으면 넣을필요업소 높이가 낮아질때 세어짐
        continue
    stack.append(y) # 높이가 다른데 높이가 높아지면 그냥 넣기

# print(stack)

while stack:
    if stack[-1] > 0:
        b_cnt += 1
    stack.pop()

print(b_cnt)