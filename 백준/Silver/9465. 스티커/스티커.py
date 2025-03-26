import sys
input = sys.stdin.readline

# 입력
T = int(input().strip())

for _ in range(T):
    N = int(input().strip())
    dp = [[0] * 3 for _ in range(N)]
    # dp[i]는 각 열에 왔을때의 스티커 점수의 최대값
    stickers = []
    for _ in range(2):
        sticker = list(map(int, input().split()))
        stickers.append(sticker)
    # print(stickers)
    k = 0
    dp[0] = [0, stickers[0][0], stickers[1][0]]
    for i in range(1, N):
        # 스티커를 떼지 않을때
        dp[i][0] = max(dp[i-1][1], dp[i-1][2], dp[i-1][0])
        # 0번 스티커를 선택하고 이전에서 안선택함, 1번선택함 중 max
        dp[i][1] = max(dp[i-1][0], dp[i-1][2]) + stickers[0][i]
        # 1번 스티커를 선택하고 이전에서 안선택함, 0번선택함 중 max
        dp[i][2] = max(dp[i-1][0], dp[i-1][1]) + stickers[1][i]
    print(max(dp[N-1]))