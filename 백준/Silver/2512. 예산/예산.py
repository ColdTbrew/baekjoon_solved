N = int(input())
reqs = list(map(int, input().split()))
total_amount = int(input())

max_amount = 0

low = 0
high = max(reqs)
def can_match(x):
    max_sum = 0
    for req in reqs:
        if req <= x:
            max_sum += req
        else:
            max_sum += x
    return max_sum

#이분 탐색
result = 0
while low<= high:
    mid = (low+high)//2
    if can_match(mid) <= total_amount:
        result = mid
        low = mid+1
    else:
        high = mid-1

print(result)