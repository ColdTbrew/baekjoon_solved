import sys
input = sys.stdin.readline


array = []
num_max = 0
max_idx = 0

for i in range(9):
    x = int(input().strip())
    array.append(x)
    if max(num_max, x) == x:
        num_max = max(num_max, x)
        max_idx = i + 1
# print(array)

print(num_max)
print(max_idx)

