# 입력 처리
N = int(input())

ans = []
def is_taller(h, ordered):
    for idx, o in enumerate(ordered):
        if h < o:
            return idx
    return -1

for _ in range(N):
    row = list(map(int, input().split()))
    caseNum = row[0]
    heights = row[1:]
    
    ordered = []
    total_go_back = 0
    for h in heights:
        if len(ordered) == 0:
            ordered.append(h)
            continue
        # print("ordered", ordered)
        new_idx = is_taller(h, ordered)
        # print("new_idx", new_idx)
        if new_idx != - 1:
            go_back = len(ordered) - new_idx
            total_go_back += go_back
            ordered.insert(new_idx, h)
        else:
            ordered.append(h)
    ans.append(total_go_back)

for idx, a in enumerate(ans):
    print(idx+1, a)

"""
1
1 901 902 903 904 905 906 907 908 909 910 911 912 913 914 915 916 917 918 919 900
"""