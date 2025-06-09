import sys
input = sys.stdin.readline

N = int(input()) # N개를 갖기 위한 금액의 최대값
cards = list(map(int, input().split()))

dp = [0] * (N+1)
# dp i 는 i개를 가질수 있을때 최대값
dp[0] = 0

for i in range(1, N+1):
    for j in range(i):
        if j+1 <= i: # i개를 만들기 위해 j+1개의 카드팩 사용가능
            dp[i] = max(dp[i], dp[i-(j+1)] + cards[j])

print(dp[N])
