import sys
input = sys.stdin.readline
from collections import deque

N = int(input())
a = list(map(int, input().split()))
print(min(a), max(a))