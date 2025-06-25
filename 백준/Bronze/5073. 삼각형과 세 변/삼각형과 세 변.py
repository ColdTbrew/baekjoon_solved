import sys
input = sys.stdin.readline

while 1:    
    a, b, c = map(int, input().split())
    if a == 0 and b == 0 and c == 0:
        exit()

    max_len = max(a, b,c)
    non_max = 0
    non_max = sum([a, b, c]) - max_len

    if non_max <= max_len:
        print("Invalid")
    elif a == b and b == c:
        print("Equilateral")
    elif a == b or b == c or a == c:
        print("Isosceles")
    else:
        print("Scalene")