N, game = input().strip().split()

apply = set()
N = int(N)
for _ in range(N):
    name = input().strip()
    apply.add(name)
people_need = 0
if game == 'Y':
    people_need = 2
elif game == 'F':
    people_need = 3
else:
    people_need = 4

print(len(apply)//(people_need-1))

