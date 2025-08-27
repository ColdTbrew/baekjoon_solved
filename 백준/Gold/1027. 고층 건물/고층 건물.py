
N = int(input())

building = list(map(int, input().split()))
# BF로 탐색할거임
# i 빌딩에서 j 빌딩을 보는데 그 사이에 빌딩들의 높이가 j 보다 낮거나 같은 빌딩들의 개수를 셈 그러면 빌딩 i가 볼수있는 빌딩의 개수가 세어지고 개수 array에 max를 구하고  
cansee = [0] * N

def slope(x1, x2, y1, y2):
    return (y2-y1)/(x2-x1)

for i in range(N):
    curH = building[i]
    
    # 오른쪽 빌딩 수 계산
    max_slope_right = float('-inf')
    visible_right = 0
    for j in range(i + 1, N):
        s = slope(i, j, curH, building[j])
        if s > max_slope_right:
            max_slope_right = s
            visible_right += 1
            
    # 왼쪽 빌딩 수 계산
    min_slope_left = float('inf')
    visible_left = 0
    for j in range(i - 1, -1, -1):
        s = slope(i, j, curH, building[j])
        if s < min_slope_left:
            min_slope_left = s
            visible_left += 1

    cansee[i] = visible_left + visible_right
    
    

# print(cansee)
print(max(cansee))