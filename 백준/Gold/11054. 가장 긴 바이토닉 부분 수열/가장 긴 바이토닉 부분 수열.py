import sys
input = sys.stdin.readline

N = int(input())
array = list(map(int, input().split()))

inc = [1] * N
des = [1] * N

for i in range(1, N):
    for j in range(i):
        if array[j] < array[i]:
            inc[i] = max(inc[i], inc[j] + 1)

for i in range(N-1, -1, -1):
    for j in range(N-1, i, -1):
        if array[j] < array[i]:
            des[i] = max(des[i], des[j] + 1)
# print(inc)
# print(des)
max_len = 0
for i in range(N):
    max_len = max(max_len, inc[i] + des[i] - 1)

print(max_len)