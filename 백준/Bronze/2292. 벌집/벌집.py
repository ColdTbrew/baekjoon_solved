import sys
input = sys.stdin.readline

N = int(input().strip())

M = 6
cur = 1

ans = 1
while cur < N:
    cur += 6 * ans
    ans += 1
    # print(cur)
print(ans)