n = int(input())
candi = list(map(int, input().split()))
import math
def is_prime(k):
    if k == 1:
        return False
    if k == 2:
        return True
    for i in range(2, int(math.sqrt(k))+1):
        if k % i == 0:
            return False
    return True

count = 0
for candy in candi:
    if is_prime(candy):
        count += 1

print(count)
