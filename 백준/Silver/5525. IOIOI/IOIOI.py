from collections import Counter
import sys
input = sys.stdin.readline


N = int(input().strip())
M = int(input().strip())
line = list(input().strip())
# print(line)
count = 0
target = list('I'+'OI'*N)
for i in range(M):
    j = i+2*N
    if j >= M:
        continue
    # print("i, j", i, j)
    hubo = line[i:j+1]
    # print("target, hubo", target, hubo)
    is_same = True
    for k in range(0, 1+2*N):
        if hubo[k] != target[k]:
            is_same = False
    if is_same:
        # print("same")
        count += 1
print(count)