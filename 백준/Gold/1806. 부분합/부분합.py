import sys 
input = sys.stdin.readline

n, s = map(int, input().split())
tree = list(map(int, input().split()))

min_len = float('inf')
current_sum = 0
left = 0

for right in range(n):
    current_sum += tree[right]

    while current_sum >= s and left <= right:
        min_len = min(min_len, right-left + 1)
        current_sum -= tree[left]
        left += 1

print(0 if min_len == float('inf') else min_len)