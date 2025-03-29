import sys
input = sys.stdin.readline

T = int(input().strip())

for _ in range(T):
    n = int(input().strip())
    gears = {}
    for i in range(n):
        name, cloth_type = input().split()
        if cloth_type in gears:
            gears[cloth_type].append(name)
        else:
            gears[cloth_type] = [name]
    from collections import Counter
    total = 1
    for key in Counter(gears):
        total *= (len(gears[key]) + 1)

    print(total-1)