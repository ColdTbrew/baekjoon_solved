import sys
input = sys.stdin.readline

# 모듈러 거듭제곱 함수
def mod_pow(base, exp, mod):
    result = 1
    base %= mod
    while exp > 0:
        if exp & 1:  # exp가 홀수면
            result = (result * base) % mod
        base = (base * base) % mod  # base를 제곱
        exp >>= 1  # exp를 반으로 줄임
    return result

L = int(input())
a = input().strip()

h = 0
mod = 1234567891

for idx, c in enumerate(a):
    h = (h + (ord(c) - 96) * mod_pow(31, idx, mod)) % mod

print(h)