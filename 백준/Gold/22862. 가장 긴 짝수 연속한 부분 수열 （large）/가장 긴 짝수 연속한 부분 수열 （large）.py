
max_len = 0
left = 0
odd_count = 0
N, K = map(int, input().split())
A = list(map(int, input().split()))
for right in range(N):
    if A[right] % 2 == 1: #홀수의 개수를 셈
        odd_count += 1
    while odd_count > K and left<=right:
        if A[left] % 2 == 1:
            odd_count -= 1 #왼쪽이 이동함으로써 홀수 개수가 넘쳤던걸 제거
        left += 1
    curr_even = (right - left +1) - odd_count
    max_len = max(max_len, curr_even)
print(max_len)

        