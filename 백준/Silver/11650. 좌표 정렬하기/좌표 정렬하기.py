n = int(input())

nums = []
for _ in range(n):
    nums.append(list(map(int, input().split())))

nums.sort(key = lambda x : (x[0], x[1]))
for n in nums:
    print(*n)