import sys
input = sys.stdin.readline

# 입력
N = int(input())

# 1. 에라토스테네스의 체로 소수 리스트 생성
M = N + 1
is_prime = [True] * M
is_prime[0] = is_prime[1] = False
for i in range(2, int(M ** 0.5) + 1):
    if is_prime[i]:
        for j in range(i * i, M, i):
            is_prime[j] = False

# 소수 리스트
primes = [i for i in range(M) if is_prime[i]]

# 2. 투 포인터로 연속된 소수의 합 계산
count = 0
left = 0
current_sum = 0
for right in range(len(primes)):
    current_sum += primes[right]
    # 합이 N보다 크면 left를 이동
    while current_sum > N and left <= right:
        current_sum -= primes[left]
        left += 1
    # 합이 N이면 경우의 수 증가
    if current_sum == N:
        count += 1

# 3. 결과 출력
print(count)