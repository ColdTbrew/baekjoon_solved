N = int(input())
buildings = list(map(int, input().split()))


ans_cnt = [0] * N
ans_idx = [float('inf')] * N


stack = [] # (높이, 인덱스) 저장
for i in range(N):
    cnt = 0
    while stack and stack[-1][0] <= buildings[i]:
        stack.pop()


    cnt = len(stack)
    ans_cnt[i] += cnt
    

    if stack:
        ans_idx[i] = stack[-1][1]
        
    stack.append((buildings[i], i))

# 오른쪽에서 왼쪽으로 순회하며 보이는 빌딩 찾기
stack = []
for i in range(N - 1, -1, -1):
    cnt = 0
    while stack and stack[-1][0] <= buildings[i]:
        stack.pop()
    
    cnt = len(stack)
    ans_cnt[i] += cnt
    
    if stack:
        # 현재 가장 가까운 빌딩 인덱스보다 더 가까운지 확인
        dist1 = abs(i - ans_idx[i])
        dist2 = abs(i - stack[-1][1])
        
        if dist1 > dist2:
            ans_idx[i] = stack[-1][1]
        elif dist1 == dist2 and ans_idx[i] > stack[-1][1]:
            ans_idx[i] = stack[-1][1]
            
    stack.append((buildings[i], i))

for i in range(N):
    if ans_cnt[i] == 0:
        print(0)
    else:
        print(ans_cnt[i], ans_idx[i] + 1)