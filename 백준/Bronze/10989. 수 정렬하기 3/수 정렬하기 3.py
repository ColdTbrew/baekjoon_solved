import sys
input = sys.stdin.readline

N = int(input())
# 정수 범위가 1~10000이라 가정 (백준 10989 기준)
count = [0] * 10001  # 0~10000까지의 빈도를 저장

# 빈도 기록
for _ in range(N):
    num = int(input())
    count[num] += 1

# 빈도 배열을 순회하며 출력
for i in range(1, 10001):
    for _ in range(count[i]):
        print(i)