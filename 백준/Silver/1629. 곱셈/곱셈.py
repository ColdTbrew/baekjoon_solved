import sys
input = sys.stdin.readline

# 입력
A, B, C = map(int, input().split())

def power(a,b,c):
    if b == 0:
        return 1 % c
    half = power(a, b//2, c)
    if b%2 == 0: # 짝수일때
        return half*half % c
    else: # 홀수 일때
        return half*half * a % c
print(power(A, B, C))