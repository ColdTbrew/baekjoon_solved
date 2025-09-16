def solution(temperature, t1, t2, a, b, onboard):
    temperature += 10
    t1 += 10
    t2 += 10
    length = len(onboard)
    temp_dp = [[float('inf')]*51 for _ in range(length)]
    temp_dp[0][temperature] = 0
    # print("temp_dp", *temp_dp, sep = '\n')
    
    def check(idx, temp) :
        return not (onboard[idx] and not t1 <= temp <= t2)
    
    for i in range(length-1) :
        for j in range(51) :
            if temp_dp[i][j] == float('inf') :
                continue
                
            # off case :
            if j < temperature :
                temp = j+1
            elif j > temperature :
                temp = j-1
            else :
                temp = j
                
            if check(i+1, temp) :
                temp_dp[i+1][temp] = min(temp_dp[i+1][temp], temp_dp[i][j])
                
            # on case :
            for temp, cost in [(j+1, a), (j-1, a), (j, b)] :
                if not check(i+1, temp) or not -1 < temp < 51 :
                    continue    
                temp_dp[i+1][temp] = min(temp_dp[i+1][temp], temp_dp[i][j] + cost)
    
    return min(temp_dp[-1])