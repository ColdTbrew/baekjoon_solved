n = int(input())
deck = list(map(int, input().split()))
m = int(input())
candi = list(map(int, input().split()))
from collections import Counter

deck_dic = Counter(deck)

for c in candi:
    if c in deck_dic:
        print("1")
    else:
        print("0")
