# 피보나치 출력 횟수 계산
T = int(input())
# DP 테이블: dp[i][0]은 0의 횟수, dp[i][1]은 1의 횟수
dp = [[0, 0] for _ in range(41)]
dp[0] = [1, 0]  # N=0: 0이 1번, 1이 0번
dp[1] = [0, 1]  # N=1: 0이 0번, 1이 1번

# DP로 0과 1의 출력 횟수 미리 계산
for i in range(2, 41):
    dp[i][0] = dp[i-1][0] + dp[i-2][0]  # 0의 횟수 = 이전 두 단계의 0 횟수 합
    dp[i][1] = dp[i-1][1] + dp[i-2][1]  # 1의 횟수 = 이전 두 단계의 1 횟수 합

# 테스트 케이스 처리
for _ in range(T):
    N = int(input())
    print(dp[N][0], dp[N][1])