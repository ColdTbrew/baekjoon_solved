N, C = map(int, input().split())
#n개의 집이 수직선 위에 있고 
# 공유기 C개를 설치하련느데
# 한집에 하나만 설치 가능하고 최대한 공유기 사이를 떨어트려놓아야함
home = []
for _ in range(N):
    x = int(input())
    home.append(x)

# 이분 탐색 사용
home.sort()

start = 1 # 최소 간격
end = home[-1] - home[0] # 최대 간격
result = 0

while start<= end:
    mid = (start+end)//2
    current = home[0] # 현재는 처음 위치
    count = 1
    for i in range(1, len(home)):
        if home[i] >= current + mid: #현재 위치 + 간격 보다 넓거나 같으면 다음 집이
            count += 1
            current = home[i]
    if count >= C: # mid씩 뛰어넘다가 c개 가 넘으면 너무 간격이 좁은거니까 start = mid + 1
        start = mid + 1
        result = mid
    else: # c개 보다 부족하면 너무 넓은거니까 end = mid
        end = mid -1
    
print(result)