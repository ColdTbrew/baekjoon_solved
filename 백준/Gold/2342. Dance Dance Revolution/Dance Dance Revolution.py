import sys
input = sys.stdin.readline

# 입력: 스텝 시퀀스 (마지막 0 포함)
steps = list(map(int, input().split()))

# 비용 함수: p에서 q로 이동하는 힘
def cost(p, q):
    if p == q: return 1  # 같은 지점
    if p == 0: return 2  # 중앙에서 이동
    if abs(p - q) == 2: return 4  # 반대편 (1↔3, 2↔4)
    return 3  # 인접 이동

# DP 배열: dp[i][l][r]는 i번째 스텝 후 왼발 l, 오른발 r일 때 최소 힘
n = len(steps) - 1  # 0 제외한 스텝 수
dp = [[[float('inf')] * 5 for _ in range(5)] for _ in range(n + 1)]
dp[0][0][0] = 0  # 초기: 두 발 중앙

# 각 스텝 처리
for i in range(n):
    if steps[i] == 0:  # 종료
        break
    target = steps[i]  # 현재 스텝의 목표 지점
    # 모든 현재 상태 (l, r) 탐색
    for l in range(5):  # 왼발 위치
        for r in range(5):  # 오른발 위치
            if dp[i][l][r] == float('inf'):  # 불가능한 상태
                continue
            # 1. 왼발로 target 누르기
            if target != r:  # 두 발이 같은 위치 불가
                dp[i + 1][target][r] = min(dp[i + 1][target][r], dp[i][l][r] + cost(l, target))
            # 2. 오른발로 target 누르기
            if target != l:  # 두 발이 같은 위치 불가
                dp[i + 1][l][target] = min(dp[i + 1][l][target], dp[i][l][r] + cost(r, target))

# 결과: 마지막 스텝의 최소 힘
result = float('inf')
for l in range(5):
    for r in range(5):
        result = min(result, dp[n][l][r])
print(result)