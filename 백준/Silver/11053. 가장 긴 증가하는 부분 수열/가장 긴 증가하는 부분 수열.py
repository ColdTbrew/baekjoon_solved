import sys
input = sys.stdin.readline

N = int(input().strip())
Aj = list(map(int, input().split()))

# dp[i]: i번째 원소로 끝나는 가장 긴 증가하는 부분 수열의 길이
# dp = [1] * N  # 자기 자신을 포함하므로 1로 초기화

dp = [1] * N
for i in range(1, N):
    for j in range(i):
        if Aj[i] > Aj[j]:
            dp[i] = max(dp[i], dp[j]+1)
# # 각 위치에서 이전 원소들과 비교
# for i in range(1, N):
#     for j in range(i):  # 0부터 i-1까지 확인
#         if Aj[j] < Aj[i]:  # 증가 조건 만족 시
#             dp[i] = max(dp[i], dp[j] + 1)  # 최대 길이 갱신
# 결과 출력
print(max(dp))