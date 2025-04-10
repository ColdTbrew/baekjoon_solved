import sys
from collections import deque
from itertools import combinations
from itertools import permutations
input = sys.stdin.readline

N = int(input().strip())
nums = list(map(int, input().split()))

opers = list(map(int, input().split()))
# print(opers)
opers_nums = []
for idx, o in enumerate(opers):
    for i in range(o):
        opers_nums.append(idx)

# print(opers_nums)
max_val = -float('inf')
min_val = float('inf')
def cal(num1, num2, op):
    if op == 0:
        return num1 + num2
    elif op == 1:
        return num1 - num2
    elif op == 2:
        return num1*num2
    else:
        if num1 < 0:
            return -(-num1 // num2)
        return num1//num2
    
for oper in permutations(opers_nums, N-1):
    result = nums[0]
    for i in range(N-1):
        result = cal(result, nums[i+1], oper[i])
    max_val = max(result, max_val)
    min_val = min(result, min_val)

print(max_val)
print(min_val)