import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)

n = int(input())
array = list(map(int, input().split()))

max_sum = array[0]
cur_sum = array[0]
for i in range(1, n):
    cur_sum = max(array[i], cur_sum + array[i])
    max_sum = max(max_sum, cur_sum)

print(max_sum)