import sys
input = sys.stdin.readline

# N = int(input().strip())

n, m = map(int, input().split())
import math

gcd = math.gcd(n, m)
print(gcd)
print(n*m//gcd)
