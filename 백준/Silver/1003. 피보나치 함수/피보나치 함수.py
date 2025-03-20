import sys
input = sys.stdin.readline

# 메모이제이션 테이블: (fib_value, zero_count, one_count) 저장
memo = [None] * 41
memo[0] = (0, 1, 0)  # fib(0): 값=0, zero=1, one=0
memo[1] = (1, 0, 1)  # fib(1): 값=1, zero=0, one=1

def fibonacci(n):
    if memo[n] is not None:
        return memo[n]
    val1, zero1, one1 = fibonacci(n-1)
    val2, zero2, one2 = fibonacci(n-2)
    memo[n] = (val1 + val2, zero1 + zero2, one1 + one2)
    return memo[n]

n = int(input().strip())
for _ in range(n):
    F = int(input().strip())
    _, zero, one = fibonacci(F)  # 값, zero, one 반환
    print(zero, one)