n, k = map(int, input().split())


table = []
for i in range(1, n+1):
    table.append(i)

keys = []
last = 0 
for _ in range(n):
    last = (last + k-1)%len(table)
    keys.append(table[last])
    del(table[last])
    # print(table)

print("<", end='')          # '<' 출력
print(*keys, sep=', ', end='')  # 요소 사이에 ', ' 삽입
print(">", end='')          # '>' 출력

"""
7 3
"""