#다솜이는 휴게소를 M개 더 지어서 휴게소가 없는 구간의 길이의 최댓값을 최소로 하려고 한다
N, M, L = map(int, input().split())
hue = list(map(int, input().split()))
hue = [0] + hue + [L]
hue.sort()
# print(hue)
# 가장 멀리 떨어져있는 = 휴게소가 없는 구간의 길이를 이분탐색으로 찾아야함
# mid가 가장 멀리 떨어져있는 거리니까 그 때의 휴게소가 몇개가 생기니까 M<count개가 high = mid생기면 정답 가능이고 M>count 보다 작게 생기면 low = mid+1
low = 1
high = L -1
result = 0
while low <= high:
    mid = (low+high)//2
    count = 0
    for i in range(1, len(hue)):
        if hue[i] - hue[i-1] > mid: #i, i+1 중간 거리가 mid 즉 가장 멀리 떨어져있는 거리 추정보다 크다면 휴게소 삽입해야함
            #사이 구간에서 mid 가 들어갈수 있는 개수만큼 휴게소 설치
            count += (hue[i] - hue[i-1] - 1)//mid
    if count > M:# 개수가 너무 많음 low를 키워야함
        low = mid + 1
    else: # 개수가 적거나 같은거니까 더 작은거 시도해야함
        high = mid -1
        result = mid
        
print(result)