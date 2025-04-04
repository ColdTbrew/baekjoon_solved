import sys
input = sys.stdin.readline

string = input().strip()
split_string = string.split('-')
# print(split_string)


split_sum = 0
for idx, s in enumerate(split_string):
    added = 0
    for i in s.split('+'):
        added += int(i)
    # print(added)
    if idx != 0:
        split_sum -= added
    else:
        split_sum = added
print(split_sum)