from itertools import product
N = int(input())

for _ in range(N):
    x = int(input())
    ops = ['+', '-', ' ']
    nums = [i+1 for i in range(x)]
    # print(nums)
    ans = []
    for select_op in product(ops, repeat=x-1):
        nums = [str(i+1) for i in range(x)]
        idx = 1
        for op in select_op:
            nums.insert(idx, op)
            idx += 2
        # 공백에 대해 먼저 숫자 이어붙이기 
        new_nums = ""
        for num in nums:
            if num == ' ': 
                continue
            else:
                new_nums += str(num)
        # print("new nums", new_nums)
        if eval(new_nums) == 0:
            ans.append(''.join(nums))
    ans.sort()
    print(*ans, sep = "\n")
    print()
