import sys
input = sys.stdin.readline

N, M = map(int, input().split())

import math
def is_prime(x):
    if x<2:
        return False
    if x == 2:
        return True
    for i in range(2, int(math.sqrt(x)) + 1):
        # print("x :", x, "i", i)
        if x % i == 0:
            return False
    return True
for i in range(N, M+1):
    if is_prime(i):
        print(i)