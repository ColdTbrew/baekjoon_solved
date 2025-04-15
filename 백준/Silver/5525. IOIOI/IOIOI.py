from collections import Counter
import sys
input = sys.stdin.readline


N = int(input().strip())
M = int(input().strip())
line = list(input().strip())
# print(line)
count = 0
i = 0

while i < M-2:
    if line[i] == 'I' and i + 2 < M and line[i+1] == 'O' and line[i+2] == 'I':
        oi_count = 0
        j = i
        while j + 2 < M and line[j+1] == 'O' and line[j+2] == 'I':
            oi_count += 1
            j += 2
        if oi_count >= N:
            count += oi_count - N + 1
        i = j
    else:
        i += 1
print(count)