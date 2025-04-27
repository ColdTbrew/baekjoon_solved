import sys
input = sys.stdin.readline
from collections import deque

N = int(input())
points = []
for i in range(N):
    x, y = map(int, input().split())
    points.append((x, y))

area = 0
for i in range(N):
    j = (i + 1) % N  # 다음 점 (마지막 점은 첫 점과 연결)
    area += points[i][0] * points[j][1]  # x_i * y_{i+1}
    area -= points[i][1] * points[j][0]  # y_i * x_{i+1}
area = round(abs(area) / 2, 1)
print(area)