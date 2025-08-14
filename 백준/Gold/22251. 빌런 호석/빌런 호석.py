n, k, p, x = map(int, input().split())

# 자릿수 맞춰주기 
if len(str(x)) < k:
    cx = '0' * (k-len(str(x))) + str(x)   
else:
    cx = str(x)

# print(cx)
nums = [[1, 1, 1, 1, 1, 1, 0], #0
        [0, 1, 1, 0, 0, 0, 0], #1
        [1, 1, 0, 1, 1, 0, 1], #2
        [1, 1, 1, 1, 0, 0, 1], #3
        [0, 1, 1, 0, 0, 1, 1], #4
        [1, 0, 1, 1, 0, 1, 1], #5
        [1, 0, 1, 1, 1, 1, 1], #6
        [1, 1, 1, 0, 0, 0, 0], #7
        [1, 1, 1, 1, 1, 1, 1], #8
        [1, 1, 1, 1, 0, 1, 1], #9
        ]
# 1 -> 2로 반전시킬때 필요한 5개를 반전시켜야함
# i -> j 로 갈때의 개수 즉, 각 위치의 led가 같지 않은 개수를 셈
arr = []
for i in range(10):
    arr.append([])
    for j in range(10):
        if i == j:
            arr[i].append(0)
        else:
            diff = 0
            for h in range(7):
                if nums[i][h] != nums[j][h]:
                    diff += 1
            arr[i].append(diff)

# print(arr)


def dfs(dep, cnt, cx):
    if dep >= len(cx): #깊이가 현재 문자열의 길이보다 크면
        if int(cx) == x: # 현재 층수와 결과가 같으면안됨
            return 0
        elif 1 <= int(cx) <= n: #1 이상 n 이하면 가능
            return 1
        else: # 그외 경우는 불가능
            return 0
    ans, cur = 0, int(cx[dep]) # 정답, 현재 바꿔줄숫자
    for i in range(10):
        if cur != i and (arr[cur][i] <= cnt): #남은 반전 가능 횟수보다 필요한 반전횟수가 작을때
            dx = cx[:dep] + str(i) + cx[dep+1:]
            ans += dfs(dep+1, cnt-arr[cur][i], dx)
        elif cur == i:
            ans += dfs(dep+1, cnt, cx)

    return ans
print(dfs(0, p, cx))