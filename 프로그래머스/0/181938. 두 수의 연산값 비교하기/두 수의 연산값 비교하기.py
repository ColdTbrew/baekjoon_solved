def solution(a, b):
    answer = 0
    left = int(str(a)+str(b))
    right = 2*a*b
    
    if left >= right:
        answer = left
    else:
        answer = right
    return answer