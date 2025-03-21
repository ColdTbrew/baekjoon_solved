import sys
input = sys.stdin.readline

N, M = map(int, input().split())
cards = list(map(int, input().split()))

result = []
pre_sum = [0] * (len(cards)+1) 
for idx, c in enumerate(cards):
    pre_sum[idx+1] = pre_sum[idx] + c

# print(pre_sum)

for _ in range(M):
    i, j = map(int, input().split())
    s = pre_sum[j] - pre_sum[i-1]
    result.append(s)

print(*result, sep = '\n')