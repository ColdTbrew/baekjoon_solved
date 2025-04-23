import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)

preorder = []
while True:
    try:
        line = sys.stdin.readline().strip()
        if not line:  # 빈 줄이면 입력 종료
            break
        preorder.append(int(line))
    except:
        break

def postorder(start, end):
    if start >= end:
        return
    root = preorder[start]
    right_start = start+1

    while right_start < end and preorder[right_start] < root:
        right_start += 1

    postorder(start+1, right_start) #왼쪽 서브트리
    postorder(right_start, end)

    print(root)

postorder(0, len(preorder))
