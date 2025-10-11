N, M = map(int, input().split())
targets = list(map(int, input().split()))

from collections import deque
count =0
nums = deque([x for x in range(1, N+1)])
# print(nums)
for target in targets:
    if nums[0] == target:
        nums.popleft()
        continue
    if nums.index(target) <= len(nums) // 2: #좌측 회전이 빠름
        # print("left shift")
        while target != nums[0]:
            nums.append(nums.popleft())
            count += 1
        nums.popleft()
    else:
        # print("right shift")
        while target != nums[0]:
            nums.appendleft(nums.pop())
            count += 1
        nums.popleft()
    # print(nums, count)
print(count)
