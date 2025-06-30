N = int(input())

graph = [ list(input().strip()) for _ in range(N)]
# print(graph)

longest_col = -1
pre_longest = -1

for j in range(N):
    count = 0 
    for i in range(N):
        if graph[i][j] == '*':
            count += 1
        else:
            if count > 0:
                break
    if count > pre_longest:
        longest_col = j
        pre_longest = count

# print("longest_col ", longest_col)

longest_row = -1
pre_longest = -1

for i in range(N):
    count = 0 
    for j in range(N):
        if graph[i][j] == '*':
            count += 1
        else:
            if count > 0:
                break
    if count > pre_longest:
        longest_row = i
        pre_longest = count

# print("longest_row ", longest_row)

#왼쪽팔은 롱기스트 로우에서 head전까지의 길이 오른팔은 헤드후에 길이
left_arm_len = 0
right_arm_len = 0
for j in range(N):
    if graph[longest_row][j] == '*':
        if j < longest_col:
            left_arm_len += 1
        elif j > longest_col:
            right_arm_len += 1

left_leg_len = 0 
right_leg_len = 0
wist = 0
for i in range(N-1, -1, -1):
    if graph[i][longest_col-1] == '*':
        left_leg_len += 1
    if graph[i][longest_col+1] == '*':
        right_leg_len += 1
    if graph[i][longest_col] == '*':
        wist += 1
print(longest_row+1, longest_col+1)
print(left_arm_len, right_arm_len,wist-2, left_leg_len-1, right_leg_len-1)