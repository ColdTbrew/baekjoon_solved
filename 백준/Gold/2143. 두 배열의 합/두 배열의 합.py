import sys
from collections import Counter
input = sys.stdin.readline

T = int(input())
n = int(input())
A = list(map(int, input().split()))
m = int(input())
B = list(map(int, input().split()))

freq_a = {}
#A 배열이 나타낼 수 있는 합들의 종류들의 횟수들
for i in range(n):
    current_sum = 0
    for j in range(i, n):
        current_sum += A[j]

        if current_sum in freq_a:
            freq_a[current_sum] += 1
        else:
            freq_a[current_sum] = 1

count = 0 #B 의 부 배열 합 계산 및 T와 쌍이 되는 경우 카운트
for i in range(m):
    current_sum = 0
    for j in range(i, m):
        current_sum += B[j]
        # T- B[j] B를 골랐을때 나머지가 A일때로 T를 만들 수 있으면 맞으니까 더해줌
        count += freq_a.get(T-current_sum, 0) # 있으면 그 빈도수 만큼 더해줌

print(count)