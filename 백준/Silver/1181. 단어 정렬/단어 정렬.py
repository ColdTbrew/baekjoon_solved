import sys
input = sys.stdin.readline

N = int(input().strip())

words = []
for i in range(N):
    x = input().strip()
    words.append(x)

words.sort(key = lambda x : [len(x), x])
s = set()
# print("---------")
for w in words:
    if w not in s:
        s.add(w)
        print(w)
