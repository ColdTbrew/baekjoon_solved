n = int(input())
m = int(input())
xs = list(map(int, input().split()))

h = 0
# x 위치를 기준으로 왼쪽 h만큼 오른쪽 h만큼 밝다 
# h를 1부터 늘려가면서 계산

street = [False] * (n+1)     
def check(h):
    # 첫 번째 가로등이 0을 커버하는지 확인
    if xs[0] - h > 0:
        return False
    # 가로등 간의 간격이 2h 이하인지 확인
    for i in range(1, m):
        if xs[i] - xs[i-1] > 2 * h:
            return False
    # 마지막 가로등이 n을 커버하는지 확인
    if xs[-1] + h < n:
        return False
    return True

low  = 0
high = n

result = n
while low <= high:
    mid = (low+high)//2
    if check(mid):
        result = mid
        high = mid -1
    else:
        low = mid + 1

print(result)