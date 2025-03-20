import sys
input = sys.stdin.readline

n, m = map(int, input().split())

dic = dict()
for _ in range(n):
    name = input().strip()
    dic[name] = 1
for _ in range(m):
    name = input().strip()
    if name in dic:
        dic[name] += 1

count  = 0 
names = []
for key, value in dic.items():
    if value == 2:
        count += 1
        names.append(key)
print(count)
names.sort()
print(*names, sep= "\n")