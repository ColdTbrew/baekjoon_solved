N = int(input())
lines = []
for _ in range(N):
    x, y = map(int, input().split())
    lines.append((x, y))

total =  0
lines.sort()
start = lines[0][0]
end = lines[0][1]
for s, e in lines[1:]:
    if s > end: # 안겹치면
        total += end - start
        start = s
        end = e
    else:
        # 겹치면 구간 늘려
        end = max(end, e)

total += end - start
        

print(total)
