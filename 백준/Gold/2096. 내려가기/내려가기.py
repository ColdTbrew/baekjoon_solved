import sys
input = sys.stdin.readline

N = int(input().strip())

# 최대/최소 점수를 위한 1차원 배열
max_dp = [0] * 3  # 초기 첫 줄 입력으로 설정
min_dp = [0] * 3

# 첫 줄 입력
max_dp = list(map(int, input().split()))
min_dp = max_dp[:]

# 나머지 N-1 줄 처리
for _ in range(N - 1):
    a, b, c = map(int, input().split())
    # 이전 값 저장
    prev_max = max_dp[:]
    prev_min = min_dp[:]
    
    # 최대값 계산
    max_dp[0] = max(prev_max[0], prev_max[1]) + a
    max_dp[1] = max(prev_max[0], prev_max[1], prev_max[2]) + b
    max_dp[2] = max(prev_max[1], prev_max[2]) + c
    
    # 최소값 계산
    min_dp[0] = min(prev_min[0], prev_min[1]) + a
    min_dp[1] = min(prev_min[0], prev_min[1], prev_min[2]) + b
    min_dp[2] = min(prev_min[1], prev_min[2]) + c

print(max(max_dp), min(min_dp))