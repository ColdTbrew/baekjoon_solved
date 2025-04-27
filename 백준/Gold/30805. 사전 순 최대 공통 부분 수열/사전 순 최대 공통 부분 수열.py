import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))

M = int(input())
B = list(map(int, input().split()))


ans = []
i, j = 0, 0
while i< N and j < M:
    max_common = -1
    nexti, nextj = -1, -1

    for a in range(i, N):
        for b in range(j, M):
            if A[a] == B[b] and max_common < A[a]:
                max_common = A[a]
                nexti = a
                nextj = b

    if max_common == -1:
        break

    ans.append(max_common)
    i, j = nexti + 1, nextj + 1

print(len(ans))
if len(ans) > 0:
    print(*ans)