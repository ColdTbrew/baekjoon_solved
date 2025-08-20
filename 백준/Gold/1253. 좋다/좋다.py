N = int(input())
array = list(map(int, input().split()))

cnt = 0
for t_idx in range(N):
    sorted_with_idx = [(val, i) for i, val in enumerate(array) if i != t_idx]
    sorted_with_idx.sort()
    
    target = array[t_idx]
    left, right = 0, len(sorted_with_idx) - 1
    
    while left < right:
        curr_sum = sorted_with_idx[left][0] + sorted_with_idx[right][0]
        if curr_sum == target:
            cnt += 1
            break
        elif curr_sum < target:
            left += 1
        else:
            right -= 1

print(cnt)