import sys

N = int(sys.stdin.readline())

expected_rank = sorted([int(input()) for _ in range(N)])
# print(expected_rank)

boolman =  0
for i in range(N):
    if expected_rank[i] != i+1:
        boolman += abs(expected_rank[i] - i - 1)
        # print("bool", abs(expected_rank[i] - i - 1))
print(boolman)
