import sys
input = sys.stdin.readline

N = int(input())
array = list(map(int, input().split()))
lis = []

for num in array:
    left, right = 0, len(lis) # lis에서 이분탐색을 통해 num이 들어갈 자리를 찾는과정
    while left < right:
        mid = (left + right) // 2 # 중간
        if lis[mid] < num: # mid보다 더 오른쪽 탐색
            left = mid + 1
        else: # mid보다 왼쪽 탐색
            right = mid
    if left == len(lis): #맨뒤에 둘꺼다
        lis.append(num)
    else:   # 그 자리를 더 작은값으로 갱신
        lis[left] = num
# print(lis)
print(len(lis))