# 수열에서 짝수섬의 길이와 과 홀수갭의 길이 추출해서 사용

N, K = map(int, input().split())
A = list(map(int, input().split()))

even_len = []
gaps = []
i = 0
while i<N:
    if A[i] % 2 == 1: #초반에 홀수면 
        i += 1
        continue
    
    # 짝수섬의 길이 계산
    start = i
    while i<N and A[i] % 2 == 0:
        i += 1
    even_len.append(i-start)

    # 홀수 갭 계산
    gap = 0
    while i<N and A[i] % 2 == 1:
        gap += 1
        i += 1
    if i<N:
        gaps.append(gap)

if not even_len:
    print(0)
else:
    max_len = 0
    left = 0
    curr_even = 0
    curr_cost = 0
    m = len(even_len)
    for right in range(m):
        curr_even += even_len[right]
        if right > left:
            curr_cost += gaps[right-1]
        while curr_cost > K and left < right:
            curr_even -= even_len[left]
            curr_cost -= gaps[left]
            left += 1
        max_len = max(max_len, curr_even)
    print(max_len)

