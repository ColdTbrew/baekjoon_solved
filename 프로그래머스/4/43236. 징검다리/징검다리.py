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
        if removed <= n:
            low = mid + 1
        else:
            high = mid - 1
    
    return high