import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)
def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, a, b):
    parent[a] = b

G = int(input())
P = int(input())
parent = list(range(G+1))

count = 0

for _ in range(P):
    g = int(input())
    root = find(parent, g)
    if root == 0:
        break
    union(parent, root, root -1)
    count += 1

print(count)