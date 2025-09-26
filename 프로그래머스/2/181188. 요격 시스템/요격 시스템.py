def solution(targets):
    answer = 0
    targets.sort(key = lambda x : x[1])
    # 끝점기준으로
    # print(targets)
    pred_end = -float('inf')
    for s, e in targets:
        if s > pred_end: #이전 마지막에서 커버가 안되는 놈이라서 새로운 미사일 필요
            answer += 1
            
            pred_end = e - 0.5
            # print(pred_end)
    return answer