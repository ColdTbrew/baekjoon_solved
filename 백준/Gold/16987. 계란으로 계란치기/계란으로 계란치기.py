N = int(input())

eggs = []
for _ in range(N):
    strength, weight = map(int, input().split())
    eggs.append([strength, weight])

def check(idxs):
    cnt = 0
    for e in eggs:
        if e[0] <= 0: # 깨진 계란 세기
            cnt += 1
    return cnt
choices_idx = []

def bt(index, arr):
    global answer

    if index == N:
        answer = max(answer, check(arr))
        return
    if arr[index][0] <= 0: # 내구도가 다 달았을때 넘어감
        bt(index+1, arr)
    else: #현재 계란의 내구도가 남아있을때 
        is_all_broken = True
        for i in range(len(arr)): # 나를 제외한 다른 계란들과 
            if index != i and eggs[i][0] > 0: 
                is_all_broken = False
                arr[index][0] -= arr[i][1]
                arr[i][0] -= arr[index][1]
                bt(index + 1, arr)
                arr[index][0] += arr[i][1]
                arr[i][0] += arr[index][1]
        if is_all_broken:
            bt(N, arr) # 모든 계란이 깨지면 바로 나오기

max_count = 0
answer = 0
bt(0, eggs)
print(answer)