T = int(input())
nums = [1, 2, 3]
tests = []
for _ in range(T):
    target = int(input())
    tests.append(target)
N = max(tests)
# 1만써서 i를 나타내는 경우
dp = [1] * (N+1)

for i in range(2, N+1):
    dp[i] = dp[i] + dp[i-2]
for i in range(3, N+1):
    dp[i] = dp[i] + dp[i-3]

# print(dp)
for x in tests:
    print(dp[x])