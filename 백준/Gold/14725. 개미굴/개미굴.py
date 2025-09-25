N = int(input())


dics = {}
for _ in range(N):
    row = input().split()
    # print(row)
    names = row[1:]
    # print(names)
    cur = dics
    for food in names:
        if food not in cur:
            cur[food] = {}
        cur = cur[food]
# print(dics)

def print_tree(dics, depth):
    for root in sorted(dics):
        print("--" * depth, end = "")
        print(root)
        print_tree(dics[root], depth+1)
    
print_tree(dics, 0)