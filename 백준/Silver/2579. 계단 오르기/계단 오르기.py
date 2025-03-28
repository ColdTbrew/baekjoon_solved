import sys
input = sys.stdin.readline

N = int(input().strip())
step = [0] * (N+1)
for i in range(1, N+1):
    x = int(input().strip())
    step[i] = x

dp = [0] * (N+1)
dp[1] = step[1]
# print(step)
if N>= 2: # 두번째 칸을 방법은 두칸 올라가기 또는 한칸 한칸 올라가기
    dp[2] = max(step[2], step[1]+ step[2])
for i in range(3, N+1): # 두칸 올라오는 경우 , 한칸 올라오는 경우는 그전 스탭이 두칸 올라오기여야하기때문
    dp[i] = max(dp[i-2], dp[i-3] + step[i-1]) + step[i]

# print(dp)
print(dp[N])