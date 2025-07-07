def ccw(x1, y1, x2, y2, x3, y3):
    return (x2 - x1) * (y3 - y1) - (y2 - y1) * (x3 - x1)

def is_intersect(seg1, seg2):
    x1, y1, x2, y2 = seg1
    x3, y3, x4, y4 = seg2
    
    # 두 선분의 CCW 계산
    ccw1 = ccw(x1, y1, x2, y2, x3, y3) * ccw(x1, y1, x2, y2, x4, y4)
    ccw2 = ccw(x3, y3, x4, y4, x1, y1) * ccw(x3, y3, x4, y4, x2, y2)
    
    # 두 선분이 한 직선 위에 있는 경우
    if ccw1 == 0 and ccw2 == 0:
        # 선분의 범위를 확인
        if min(x1, x2) <= max(x3, x4) and min(x3, x4) <= max(x1, x2) and \
           min(y1, y2) <= max(y3, y4) and min(y3, y4) <= max(y1, y2):
            return True
        return False
    
    # 교차 여부 판단
    return ccw1 <= 0 and ccw2 <= 0

def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, rank, x, y):
    px, py = find(parent, x), find(parent, y)
    if px == py:
        return
    if rank[px] < rank[py]:
        px, py = py, px
    parent[py] = px
    if rank[px] == rank[py]:
        rank[px] += 1

def main():
    N = int(input())
    segments = []
    for _ in range(N):
        x1, y1, x2, y2 = map(int, input().split())
        segments.append((x1, y1, x2, y2))
    
    # 유니온-파인드 초기화
    parent = list(range(N))
    rank = [0] * N
    
    # 모든 선분 쌍에 대해 교차 여부 확인
    for i in range(N):
        for j in range(i + 1, N):
            if is_intersect(segments[i], segments[j]):
                union(parent, rank, i, j)
    
    # 그룹 수와 최대 그룹 크기 계산
    groups = {}
    for i in range(N):
        root = find(parent, i)
        groups[root] = groups.get(root, 0) + 1
    
    print(len(groups))  # 그룹 수
    print(max(groups.values()))  # 최대 그룹 크기

if __name__ == "__main__":
    main()