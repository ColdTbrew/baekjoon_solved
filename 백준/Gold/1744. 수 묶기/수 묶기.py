N = int(input())

array = []
for _ in range(N):
    x = int(input())
    array.append(x)

pos = []
neg = []
zero_exist = False


ans = 0
for x in array:
    if x > 1:
        pos.append(x)
    elif x == 1:
        ans += 1
    elif x == 0:
        zero_exist = True
    else:
        neg.append(x)

pos.sort(reverse=True)
for i in range(0, len(pos), 2):
    if i + 1 < len(pos):
        ans += pos[i] * pos[i+1]
    else:
        ans += pos[i]

neg.sort() # 제일 작은 음수 끼리 곱하면 제일 큰 양수됨
for i in range(0, len(neg), 2):
    if i + 1 < len(neg):
        ans += neg[i] * neg[i+1]
    else:
        if not zero_exist:
            ans += neg[i]
print(ans)