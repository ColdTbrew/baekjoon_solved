import sys
input = sys.stdin.readline
from collections import deque

N = int(input())
liquid = list(map(int, input().split()))

i, j = 0, N-1
min_diff = float('inf')
min_a, min_b = 0, 0
while i < j:
    current_sum = liquid[i] + liquid[j]
    diff = abs(current_sum)
    
    # 최소 차이 갱신
    if diff < min_diff:
        min_diff = diff
        min_a, min_b = liquid[i], liquid[j]
    
    # 합에 따라 투 포인터 이동
    if current_sum < 0:
        i += 1
    elif current_sum > 0:
        j -= 1
    else:
        break

print(min_a, min_b)