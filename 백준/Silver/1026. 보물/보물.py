N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# B_with_order = [(b, idx) for idx, b in enumerate(B)]
# print(B_with_order)
# B_with_order.sort(key = lambda x : x[0])
# print(B_with_order)
B.sort()
A.sort()
A.reverse()

s = 0
for i in range(N):
    s += A[i] * B[i]
print(s)