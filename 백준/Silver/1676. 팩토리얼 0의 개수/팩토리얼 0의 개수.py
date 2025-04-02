import sys
input = sys.stdin.readline

N = int(input().strip())

import math
num = list(str(math.factorial(N)))

count = 0
num.reverse()
# print(num)
for n in num:
    if n != '0':
        print(count)
        break
    else:
        count += 1