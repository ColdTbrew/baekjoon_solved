from itertools import combinations
def solution(n, q, ans):
    answer = 0
    for secret in combinations(list(range(1,n+1)), 5):
        valid = True
        for idx in range(len(q)):
            if len(set(q[idx]) & set(secret)) != ans[idx]:
                valid = False
    
        if valid:
            answer+= 1
    return answer