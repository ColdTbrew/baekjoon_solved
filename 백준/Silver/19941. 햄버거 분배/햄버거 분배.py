N, K = map(int, input().split())
table = input().strip()
ate_table = [False for _ in range(N)]
people_count = 0

for idx in range(N):
    if table[idx] == 'P':
        for r in range(-K, K+1):
            if 0<= idx+r < N:
                reach = table[idx+r]
                # print("reach", reach)
                if reach == 'H' and ate_table[idx+r] == False:
                    ate_table[idx+r] = True
                    people_count += 1
                    break

# print(ate_table)
print(people_count)
