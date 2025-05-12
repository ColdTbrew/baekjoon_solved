import sys
input = sys.stdin.readline

N = int(input())
x = list(map(int, input().split()))
M = max(x)  # 최대 카드 값
sieve = [0] * (M + 1)  # 점수 배열
S = set(x)  # 빠른 조회를 위한 집합

# 배수 탐색으로 점수 계산
for i in x:
    if i == M:
        continue
    for j in range(i * 2, M + 1, i):
        if j in S:
            sieve[i] += 1
            sieve[j] -= 1

# 결과 출력
for i in x:
    print(sieve[i], end=' ')