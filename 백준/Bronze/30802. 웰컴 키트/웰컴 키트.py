n = int(input())
s, m, l, xl, xxl, xxxl = list(map(int, input().split()))

T, P = list(map(int, input().split()))

sizes = [s, m, l, xl, xxl, xxxl]
tgroup = 0
import math
for s in sizes:
    tgroup += math.ceil(s/T)

print(tgroup)
pgroup = n//P
pen = n%P
print(pgroup,pen)