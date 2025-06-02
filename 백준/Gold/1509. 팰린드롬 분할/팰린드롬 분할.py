import sys
input = sys.stdin.readline

S = input().strip()
N = len(S)

is_palindrome = [[False] * N for _ in range(N)]

for i in range(N):
    is_palindrome[i][i] = True

for length in range(2, N+1):
    for start in range(N-length + 1):
        end = start + length - 1
        if length == 2:
            is_palindrome[start][end] = (S[start] == S[end])
        else:
            is_palindrome[start][end] = (S[start] == S[end]) and is_palindrome[start+1][end-1]
    
dp = [float('inf')] * N
dp.insert(0, 0)

for i in range(N):
    for j in range(i+1):
        if is_palindrome[j][i]:
            dp[i+1] = min(dp[i+1], dp[j-1+1] + 1)


print(dp[N])