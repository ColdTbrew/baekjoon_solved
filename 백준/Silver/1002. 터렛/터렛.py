import sys
input = sys.stdin.readline

# 테스트 케이스 수 입력
T = int(input())

for _ in range(T):
    # 입력: x1, y1, r1, x2, y2, r2
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    
    # 두 점 사이의 거리 계산
    d = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
    
    # 두 원의 반지름 합과 차
    r_sum = r1 + r2
    r_diff = abs(r1 - r2)
    
    # 경우의 수 처리
    if d == 0 and r1 == r2:  # 두 원이 동일 (무한대 교점)
        print(-1)
    elif d == r_sum or d == r_diff:  # 외접 또는 내접 (한 점에서 만남)
        print(1)
    elif r_diff < d < r_sum:  # 두 점에서 만남
        print(2)
    else:  # 만나지 않음 (외부 또는 내부 포함)
        print(0)