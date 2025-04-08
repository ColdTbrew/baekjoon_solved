import sys
input = sys.stdin.readline

N = int(input().strip())

classes = list(map(int, input().split()))

B, C = map(int, input().split())

total_t = 0
import copy
for people in classes:
    total_t += 1
    remaining = people - B
    if remaining > 0:
        total_t += remaining // C
        if remaining % C> 0:
            total_t += 1


print(total_t)
