import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))

dp = [1] * N  # 각 위치에서 LIS의 길이
prev = [-1] * N  # 이전 인덱스를 저장하여 경로 추적

# DP를 이용해 LIS 길이와 경로 추적 정보 저장
for i in range(N):
    for j in range(i):
        if A[j] < A[i] and dp[j] + 1 > dp[i]:
            dp[i] = dp[j] + 1
            prev[i] = j

# LIS의 최대 길이와 그 끝 인덱스 찾기
max_len = max(dp)
idx = dp.index(max_len)

# LIS 구성 수열 추적
sequence = []
while idx != -1:
    sequence.append(A[idx])
    idx = prev[idx]

sequence.reverse()

print(max_len)
print(*sequence)
