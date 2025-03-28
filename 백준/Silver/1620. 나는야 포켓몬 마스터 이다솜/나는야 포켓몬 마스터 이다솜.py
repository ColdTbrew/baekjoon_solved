import sys
input = sys.stdin.readline

N, M = map(int, input().split())
name_to_num = {}
num_to_name = {}
for i in range(1, N+1):
    x = input().strip()
    name_to_num[x] = i
    num_to_name[i] = x

for _ in range(M):
    q = input().strip()
    if 'A' <= q[0] <= 'Z':
        print(name_to_num[q])
    else:
        print(num_to_name[int(q)])