left_nums = input().strip()

left_ptr = 0
for N in range(1, 100000):
    n_str = str(N)
    for c in n_str:
        if left_ptr < len(left_nums) and c == left_nums[left_ptr]:
            left_ptr += 1
    if left_ptr == len(left_nums):
        print(N)
        break
    