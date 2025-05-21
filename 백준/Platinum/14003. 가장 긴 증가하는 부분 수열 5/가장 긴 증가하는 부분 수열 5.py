N = int(input())
array = list(map(int, input().split()))
ans = []
# 경로 추적용
index_trace = []
for i in range(N):
    num = array[i]
    left = 0
    right = len(ans)
    while left < right:
        mid = (left+right)//2
        if num > ans[mid][0]:
            left = mid + 1
        else:
            right = mid
    if left == len(ans):
        ans.append((num, i))
    else:
        ans[left] = (num, i)
    index_trace.append((i, left))

# print(index_trace)
print(len(ans))
# print(*ans)

lis = []
target_pos = len(ans) -1 #LIS의 마지막 위치부터 시작

for i in range(N-1, -1, -1): # 뒤에서 부
    if index_trace[i][1] == target_pos:
        lis.append(array[i])
        target_pos -= 1
    if target_pos < 0:
        break

print(*lis[::-1])
