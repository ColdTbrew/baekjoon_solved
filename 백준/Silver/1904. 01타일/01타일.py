import sys

x = int(input())
dp = [0] * (x+1)

if x <= 2:
    print(x)
    exit()
if x == 3:
    print(3)
    exit()
if x == 4:
    print(5)
    exit()


a, b = 1, 2

for i in range(3, x+1):
    c = (a + b) %15746
    a, b = b, c

print(c) 