import sys
input = sys.stdin.readline

N = int(input().strip())

db = [ list(input().split()) for _ in range(N)]
# print(db)
db.sort(key = lambda x: [int(x[0])])

for d in db:
    print(*d)
