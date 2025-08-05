H, W = map(int, input().split())
blocks = list(map(int, input().split()))

# 내 차례가 왔을때 
# 내 블럭 위에 비의 양은 (min(왼쪽에서 가장 높은 벽 , 오른쪽에서 가장 높은 벽) - 내 높이)


water = 0
for cur in range(0, W):
    # 왼쪽에서 가장 높은 벽 찾기
    left_high = 0
    for left in range(0, cur):
        if blocks[left] > left_high:
            left_high = blocks[left]
    # 오른쪽에서 가장 높은 벽 찾기
    right_high = 0
    for right in range(cur+1, W):
        if blocks[right] > right_high:
            right_high = blocks[right]
    
    if left_high > 0 and right_high >0 :
        min_high = min(left_high, right_high)
        if min_high > 0 and min_high - blocks[cur] > 0:
            water += min_high - blocks[cur]
            # print(min_high - blocks[cur])
print(water)