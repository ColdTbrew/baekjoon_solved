def solution(words):
    words.sort()
    def lcp(a,b):
        l = 0
        for x,y in zip(a,b):
            if x==y: l+=1
            else: break
        return l

    answer=0
    for i,w in enumerate(words):
        left = lcp(w, words[i-1]) if i>0 else 0
        right = lcp(w, words[i+1]) if i<len(words)-1 else 0
        need = max(left, right)+1
        answer += min(need, len(w))
    return answer