import sys
input = sys.stdin.readline

def z_order(n, r, c):
    if n == 1:  # 2×2 배열 기본 케이스
        mapping = [[0, 1], [2, 3]]  # Z순서: 왼위(0), 오위(1), 왼아(2), 오아(3)
        return mapping[r][c]
    
    half = 2 ** (n - 1)  # 사분면 크기
    quadrant_size = half * half  # 각 사분면의 칸 수
    
    # 사분면 판단
    if r < half and c < half:  # 1사분면
        return z_order(n - 1, r, c)
    elif r < half and c >= half:  # 2사분면
        return quadrant_size + z_order(n - 1, r, c - half)
    elif r >= half and c < half:  # 3사분면
        return 2 * quadrant_size + z_order(n - 1, r - half, c)
    else:  # 4사분면
        return 3 * quadrant_size + z_order(n - 1, r - half, c - half)

N, r, c = map(int, input().split())
result = z_order(N, r, c)
print(result)