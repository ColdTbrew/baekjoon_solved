import sys
input = sys.stdin.readline

n = int(input())
q = list(map(int, input().split()))

time = 0
total_time = 0
q.sort()
for p in q:
    time += p
    total_time += time

print(total_time)