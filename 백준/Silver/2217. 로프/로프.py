import sys
input = sys.stdin.readline

N = int(input())
ropes = []
for _ in range(N):
    ropes.append(int(input()))

ropes.sort(reverse=True)

max_weight = 0
for i in range(len(ropes)):
    rope_count = i +1
    weakest_rope = ropes[i]

    cur_max = weakest_rope * rope_count
    max_weight= max(max_weight, cur_max)

print(max_weight)