import sys

def solve():
    nums = list(map(int, sys.stdin.readline().split()))
    
    is_ascending = True
    is_descending = True
    
    for i in range(len(nums) - 1):
        if nums[i] + 1 != nums[i+1]:
            is_ascending = False
        if nums[i] - 1 != nums[i+1]:
            is_descending = False
    
    if is_ascending:
        print("ascending")
    elif is_descending:
        print("descending")
    else:
        print("mixed")

solve()