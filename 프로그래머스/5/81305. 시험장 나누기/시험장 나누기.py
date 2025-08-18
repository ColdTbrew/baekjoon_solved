import sys
sys.setrecursionlimit(int(1e6))
                                       
    
def find_root(links):
    length = len(links)
    visited = [False] * length
    for i in range(length):
        if not visited[i]:
            result = i
            q = [i]
            visited[i] = 0
            while q:
                node = q.pop()
                for leaf in links[node]:
                    if leaf > -1 and not visited[leaf]:
                        visited[leaf] = True
                        q.append(leaf)
    return result
def search(node, target, num, links):
    if node == -1:
        return 0, 0
    l, r = links[node]
    l_cnt, l_val = search(l, target, num, links)
    r_cnt, r_val = search(r, target, num, links)
    tot_cnt = l_cnt + r_cnt
    
    result_sum = l_val + r_val + num[node]
    
    if result_sum <= target:
        return tot_cnt, result_sum
    
    if min(l_val, r_val) + num[node] <= target:
        return tot_cnt + 1, min(l_val, r_val) + num[node]
    
    return tot_cnt+2, num[node]

def binary_search(root, start, end, k, num, links) :
    result = end
    while start <= end :
        mid = (start + end) // 2
        div_cnt, _ = search(root, mid, num, links)
        if div_cnt > k-1 : #k-1 보다 많이 나눠져있을때 
            start = mid+1
        else :
            result = min(result, mid) #최소 찾기
            end = mid-1 
    
    return result

                                       
def solution(k, num, links):
    root = find_root(links)
    start, end = max(num), sum(num)
    answer = binary_search(root, start, end, k, num, links)
    
    
    return answer