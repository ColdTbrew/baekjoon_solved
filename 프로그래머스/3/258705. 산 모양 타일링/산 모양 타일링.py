def solution(n, tops):
    answer = 0
    dp = [0] * (2*n+1)
    dp[0] = 1
    dp[1] = 3 if tops[0] == 1 else 2
    dp[2] = 7
    for i in range(2, 2*n+1):
        if i % 2 == 1 and tops[i//2] == 1: # 위에 머리가 있는 부분은 dp[i-1] * 2배
            dp[i] = dp[i-1] * 2 + dp[i-2]
        else:   
            dp[i] = (dp[i-1] + dp[i-2])%10007
    answer = dp[2*n]
    return answer