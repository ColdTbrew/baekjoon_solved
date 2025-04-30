import sys
input = sys.stdin.readline
from collections import deque

N = int(input())
a = list(map(int, input().split()))
# 3포인터를 사용해보자
a.sort()
# print(a)
all_min = float('inf')
ans = []
for i in range(0, N-2):

    j = i + 1
    k = N - 1
    while j < k:
        # print(a[i], a[j] ,a[k])
        cur_min = a[i] + a[j] + a[k]
        # print(cur_min)
        if abs(cur_min) < all_min:
            all_min = abs(cur_min)
            ans.append((i, j, k))
        if cur_min < 0:
            j += 1
        elif cur_min > 0:
            k -= 1
        else:
            i, j, k = ans[-1]
            print(a[i], a[j], a[k])
            exit()

i, j, k = ans[-1]
print(a[i], a[j], a[k])