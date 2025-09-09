T = list(input().strip())
S = list(input().strip())

count = 0
i = 0
sl = len(S)
tl = len(T)
while(tl - sl >= i):
    if T[i:i+sl] == S:
        count += 1
        i += sl
    else:
        i += 1
print(count)