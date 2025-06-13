import sys
input = sys.stdin.readline

array = list(map(int, input().split()))
sum = 0

for a in array:
    sum += a**2

print(sum%10)