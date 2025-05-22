def count_ones(n):
    if n < 0: return 0
    total = 0
    for k in range(64):  # 10^16 < 2^64
        period = 1 << (k + 1)  # 2^(k+1)
        ones = (n // period) * (1 << k)  # 완전한 주기에서 1의 개수
        remainder = n % period
        if remainder >= (1 << k):
            ones += remainder - (1 << k) + 1
        total += ones
    return total

A, B = map(int, input().split())
print(count_ones(B) - count_ones(A - 1))