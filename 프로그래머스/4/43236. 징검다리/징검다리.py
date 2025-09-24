def solution(distance, rocks, n):
    low = 1
    high = distance
    rocks.sort()
    rocks = [0] + list(rocks) + [distance]
    while low <= high:
        mid = (low + high)//2
        prev = 0
        removed = 0
        # 현재와 그전꺼랑 빼서 거리를 예상보다 작은지 검사해서 작은놈이면 삭제하고 
        # 그렇지 않으면 prev = rocks[idx]
        for idx in range(1, len(rocks)):
            if rocks[idx] - prev < mid:
                removed += 1
            else:
                prev = rocks[idx] 
        if removed <= n:#가능 케이스, 제거한 바위 수가 n 이하 → mid가 가능하므로 더 큰 값 탐색 (low = mid + 1).
            low = mid + 1
        else: #불가능 케이스, 제거한 바위 수가 n 초과 → mid가 너무 크므로 범위 축소 (high = mid - 1).
            high = mid - 1
        print("try mid ", mid)
        print("low", low)
        print("high", high)
    return high
# 탐색이 끝날 때, high는 조건을 만족하는 최대 mid 값(즉, 최대화된 최소 거리)을 가리킴.
# low는 high + 1이 되어 조건을 만족하지 않는 첫 번째 값(너무 큰 최소 거리)을 가리킴.