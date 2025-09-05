N, M = map(int, input().split())
# 1부터 N까지의 자연수중 중복없이 M개를 고른 수열
cur = []
ans = []

def bt():
    if len(cur) == M:
        temp = cur[:]
        ans.append(temp)
        
        return
    for i in range(1, N+1):
        if i not in cur:
            cur.append(i)
            bt()
            cur.pop()

bt()
ans.sort()
for a in ans:
    print(*a)
