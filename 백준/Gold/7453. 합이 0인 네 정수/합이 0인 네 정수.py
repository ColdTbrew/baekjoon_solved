import sys
input = sys.stdin.readline

N = int(input())
count = 0
#AB = -CD
AB = []
CD = []
A,B,C,D = [],[],[],[]
for _ in range(N):
    a, b, c, d = map(int, input().split())
    A.append(a)
    B.append(b)
    C.append(c)
    D.append(d)

for i in range(N):
    for j in range(N):
        AB.append(A[i]+B[j])
        CD.append(C[i]+D[j])
from collections import Counter
CD_count = Counter(CD)

for n in AB:
    count += CD_count[-n]
    
print(count)
