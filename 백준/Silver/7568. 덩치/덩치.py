import sys
input = sys.stdin.readline

N = int(input().strip())

nums = [list(map(int,input().split())) for _ in range(N)]

# print(nums)
ans = []
for i in range(N): 
    count = 1
    me_w, me_h = nums[i]
    for idx, spec in enumerate(nums):
        if i != idx:
            if me_w < spec[0] and me_h < spec[1]:
                count += 1
    ans.append(count)

print(*ans)