import sys
input = sys.stdin.readline

N = int(input().strip())
from collections import Counter
cor = list(map(int, input().split()))
cor_sorted = sorted(cor)
dic = dict()
order =  0
for c in cor_sorted:
    if c not in dic:
        dic[c] = order
        order += 1

# print(dic)
for c in cor:
    print(dic[c], end = " ")