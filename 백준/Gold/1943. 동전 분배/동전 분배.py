def can_divide(coins):
    total = sum(v*c for v, c in coins)
    if total % 2 != 0:
        return 0
    target = total//2
    dp = [False] * (target+1)
    dp[0] = True
    for v, count in coins:
        k = 1
        while count > 0:
            use = min(k, count)
            coin_value = v * use
            for i in range(target, coin_value-1, -1):
                if dp[i-coin_value]: dp[i] = True
            count -= use
            k *= 2
    # print(dp)
    return 1 if dp[target] else 0

for _ in range(3):
    N = int(input())
    coins = []
    for _ in range(N):
        coin, count = map(int, input().split())
        coins.append((coin, count))
    print(can_divide(coins))