import sys
input = sys.stdin.readline

N = int(input())
array = []

for _ in range(N):
    x = int(input())
    array.append(x)

print(int(round(sum(array)/N, 0)))
print(sorted(array)[N//2])
from collections import Counter
counter = Counter(array)
max_freq = counter.most_common(1)[0][1]
modes = sorted([key for key, freq in counter.items() if freq == max_freq])
if len(modes) > 1:
    print(modes[1])
else:
    print(modes[0])

print(max(array)-min(array))