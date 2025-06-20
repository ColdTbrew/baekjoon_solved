i, j, n, m = map(int, input().split())

count = 0
rc = i//(n+1) if i%(n+1) == 0 else i//(n+1) + 1
# print(rc)
cc = j//(m+1) if j%(m+1) == 0 else j//(m+1) + 1
# print(cc)
print(rc*cc)