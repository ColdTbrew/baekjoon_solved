N = int(input())

x = list(map(int, input().strip()))
target = list(map(int, input().strip()))

# 그리디면

def change(x, target):
    cnt1 = 0
    for i in range(1, N):
        # i - 1 전구가 같으면 넘어감
        if target[i-1] == x[i-1]:
            continue
        cnt1 += 1
        # 다르면 뒤집기 하기
        for j in range(i-1, i+2):
            if j< N:
                x[j] = 1- x[j]

    return cnt1 if x == target else 1e9

#첫번째 스위치를 누르지 않을때
cnt1 = change(x[:], target)
x[0] = 1-x[0]
x[1] = 1-x[1]
ans = min(change(x[:], target)+1, cnt1)

print(ans if ans != 1e9 else -1)