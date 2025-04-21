import sys
import math

input = sys.stdin.readline

A, B, V = map(int, input().split())

# (V-B) / (A-B)를 올림
days = math.ceil((V - B) / (A - B))

print(days)