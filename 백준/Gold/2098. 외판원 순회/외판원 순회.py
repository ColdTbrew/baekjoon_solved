import sys
input = sys.stdin.readline

def tsp(n, dist):
    #dp[visited][curr] : 방문상태 visited 에서 현재 도시 curr에 있을때의 최소 비용
    dp = [[None]*n for _ in range(1<<n)]

    def solve(visited, curr):
        # 모든 도시를 방문한경우 시작점으로 돌아가는 비용
        if visited == (1<<n) -1:
            return dist[curr][0] if dist[curr][0] else float('inf')
        
        # 이미 계산된 경우 반환
        if dp[visited][curr] is not None:
            return dp[visited][curr]
        
        #다음 도시로 이동하며 최소 비용 계산
        min_cost = float('inf')
        for next_city in range(n):
            # 방문하지 않았고 거리가 양수이면 코스트 구함
            if not(visited & (1<<next_city)) and dist[curr][next_city] > 0:
                cost = dist[curr][next_city] + solve(visited | (1<< next_city), next_city)

                min_cost = min(min_cost , cost)

        dp[visited][curr] = min_cost
        return min_cost
    return solve(1<<0, 0)

n = int(input())
dist = [list(map(int, input().split())) for _ in range(n)]

# 결과 출력
result = tsp(n, dist)
print(result)