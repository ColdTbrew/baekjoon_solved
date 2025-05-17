mod = 10**9
max_n = 101
all_used = (1 << 10) -1

dp = [[[0] * (1 << 10) for _ in range(10)]for _ in range(max_n)]

N = int(input())

for i in range(1, 10):
    dp[0][i][1<<i] = 1

for pos in range(N-1):
    for last in range(10):
        for used in range(1<<10):
            if dp[pos][last][used] == 0:
                continue
            if last -1 >= 0:
                next_num = last -1
                new_used = used | (1<< next_num)
                dp[pos + 1][next_num][new_used] = (dp[pos+1][next_num][new_used] + dp[pos][last][used]) % mod
            if last+1 <= 9:
                next_num = last + 1
                new_used = used | (1<< next_num)
                dp[pos + 1][next_num][new_used] = (dp[pos+1][next_num][new_used] + dp[pos][last][used]) % mod

ans = 0
for last in range(10):
    ans = (ans + dp[N - 1][last][all_used]) % mod

print(ans)