# 0 or 1의 그룹의 개수를 세서 적은 그룹수를 리턴
A = list(input().strip())
one_count = 0
zero_count = 0

last = A[0]

for a in A[1:]:
    if a == last:
        continue
    if a == '1':
        zero_count += 1
        last = '1'
    else:
        one_count += 1
        last = '0'

if A[-1] == '0': zero_count += 1
else: one_count += 1
# print(one_count, zero_count)
print(min(one_count, zero_count))