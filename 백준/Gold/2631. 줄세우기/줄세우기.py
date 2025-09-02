N = int(input())
line = [int(input()) for _ in range(N)]
# print(line)

dp = [1] * (N+1) # i번째에서의 최대 증가수열의 길이를 담음 그래서 항상1부터 시작
for i in range(0, N):
    for j in range(0, i):
        if line[i] > line[j]:
            dp[i] = max(dp[i], dp[j] + 1)

# print(dp)
print(N-max(dp))