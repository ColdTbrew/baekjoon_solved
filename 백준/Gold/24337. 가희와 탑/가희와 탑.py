N, a, b = map(int, input().split())
answer = []

# N 고려 안하고 제일 간단하게 조건 만족시키기
for i in range(1, a):
    answer.append(i)
answer.append(max(a, b))
for i in range(b-1, 0, -1):
    answer.append(i)

if len(answer) > N: # 조건이 만족이 안되는 경우
    print(-1)
else:
    print(answer[0], end=" ")
    for i in range(N-len(answer)): # 핵심 포인트
        print(1, end=" ")
    for i in range(1, len(answer)):
        print(answer[i], end=" ")
