import sys
input = sys.stdin.readline

def ccw(x1, y1, x2, y2, x3, y3):
    return (x2 - x1) * (y3 - y1) - (y2 - y1) * (x3 - x1)

x1, y1, x2, y2 = map(int, input().split())
x3, y3, x4, y4 = map(int, input().split())

# L1 기준 CCW
ccw1 = ccw(x1, y1, x2, y2, x3, y3)
ccw2 = ccw(x1, y1, x2, y2, x4, y4)
# L2 기준 CCW
ccw3 = ccw(x3, y3, x4, y4, x1, y1)
ccw4 = ccw(x3, y3, x4, y4, x2, y2)

# 교차 여부 판단
if ccw1 * ccw2 <= 0 and ccw3 * ccw4 <= 0:
    # 일직선인 경우 (CCW 값이 모두 0)
    if ccw1 == 0 and ccw2 == 0 and ccw3 == 0 and ccw4 == 0:
        # x, y 범위 확인
        if (max(x1, x2) >= min(x3, x4) and max(x3, x4) >= min(x1, x2) and
            max(y1, y2) >= min(y3, y4) and max(y3, y4) >= min(y1, y2)):
            print(1)
        else:
            print(0)
    else:
        print(1)
else:
    print(0)