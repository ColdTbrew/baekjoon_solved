def solution(info, n, m):
    # dp[j] = A 도둑의 누적 흔적이 j일 때, B 도둑의 최소 누적 흔적
    # A의 흔적이 n 미만이어야 하므로 n까지, 즉 n+1 크기로 dp 배열을 만듭니다.
    dp = [float('inf')] * (n + 1)
    dp[0] = 0

    for ah, bh in info:
        new_dp = [float('inf')] * (n + 1)
        
        for j in range(n + 1):
            if dp[j] != float('inf'):
                # 1. A 도둑이 현재 물건을 가져가는 경우
                if j + ah < n:
                    new_dp[j + ah] = min(new_dp[j + ah], dp[j])
                
                # 2. B 도둑이 현재 물건을 가져가는 경우
                if dp[j] + bh < m:
                    new_dp[j] = min(new_dp[j], dp[j] + bh)
        
        # 새로운 dp 테이블로 갱신
        dp = new_dp
    
    # 최종 결과 찾기: A의 흔적이 유효하면서 B의 흔적도 m 미만인 경우 중, A의 최소 흔적을 찾습니다.
    min_cura = float('inf')
    for cura in range(n + 1):
        if dp[cura] != float('inf') and dp[cura] < m:
            min_cura = min(min_cura, cura)

    if min_cura == float('inf'):
        return -1
    else:
        return min_cura