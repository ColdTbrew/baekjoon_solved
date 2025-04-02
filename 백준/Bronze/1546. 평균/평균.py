import sys
input = sys.stdin.readline

N = int(input().strip())

db = list(map(int, input().split()))
max_num = max(db)
for idx, d in enumerate(db):
    d = d/max_num * 100
    db[idx] = d
print(sum(db)/len(db))
