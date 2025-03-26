import sys
input = sys.stdin.readline

# 입력
N = int(input().strip())
tree = {}

for _ in range(N):
    parent, left, right = input().split()
    tree[parent] = [left, right]

#preorder
def preorder(root):
    if root == ".":
        return
    print(root, end='')
    preorder(tree[root][0])
    preorder(tree[root][1])

def inorder(root):
    if root == ".":
        return
    inorder(tree[root][0])
    print(root, end='')
    inorder(tree[root][1])

def postorder(root):
    if root == ".":
        return
    postorder(tree[root][0])
    postorder(tree[root][1])
    print(root, end='')

preorder('A')
print()
inorder('A')
print()
postorder('A')