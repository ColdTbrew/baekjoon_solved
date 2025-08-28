import sys

N = int(sys.stdin.readline())
mod = 1_000_000_000

# F(n) = F(n-1) + F(n-2)
# F(0) = 0
# F(1) = 1

if N == 0:
    print(0)
    print(0)
else:
    abs_N = abs(N)
    
    # 0 이상의 피보나치 수열을 계산
    dp = [0] * (abs_N + 1)
    if abs_N > 0:
        dp[1] = 1

    for i in range(2, abs_N + 1):
        dp[i] = (dp[i-1] + dp[i-2]) % mod

    fib_n_abs = dp[abs_N]

    if N > 0:
        print(1)
        print(fib_n_abs)
    else: # N < 0
        # 음의 피보나치 수의 부호 규칙: F(-n) = (-1)^(n+1) * F(n)
        if abs_N % 2 == 0: # n이 짝수일 때
            print(-1)
            print(fib_n_abs)
        else: # n이 홀수일 때
            print(1)
            print(fib_n_abs)