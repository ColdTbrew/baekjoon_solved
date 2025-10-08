from collections import deque

def solution(nodeinfo):
    answer = [[], []]
    nodes = [[nodeinfo[i][0], nodeinfo[i][1], i + 1] for i in range(len(nodeinfo))]
    nodes = sorted(nodes, key=lambda k: (-k[1], k[0]))
    
    mdict = {}
    for x, y, idx in nodes:  # Tree 만들기
        mdict[idx] = [x, y, None, None]  # [x, y, left, right]
        curr = nodes[0][2]
        while True:
            if x > mdict[curr][0]:  # right child
                if mdict[curr][3] is None:  # child가 없으면 추가
                    mdict[curr][3] = idx
                    break
                curr = mdict[curr][3]
            elif x < mdict[curr][0]:  # left child
                if mdict[curr][2] is None:  # child가 없으면 추가
                    mdict[curr][2] = idx
                    break
                curr = mdict[curr][2]
            else:
                break

    for idx, order in enumerate([[3, 2], [2, 3]]):  # 0: preorder, 1: postorder
        stack = [nodes[0][2]]  # root node
        result = deque()
        while stack:
            curr = stack.pop()
            if idx == 0:
                result.append(curr)  # preorder 결과
            else:
                result.appendleft(curr)  # postorder 결과
                
            for child in order:  # child 확인 순서
                if mdict[curr][child] is not None:  # child가 있으면 추가
                    stack.append(mdict[curr][child])
        answer[idx] = list(result)
    return answer