S = int(input())

N = 1
total = 0
while total <= S:
    total += N
    if total > S:
        break
    N += 1

print(N - 1)