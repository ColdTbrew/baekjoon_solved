import sys
input = sys.stdin.readline

# 점수 입력
score = int(input().strip())

# 등급 결정
if 90 <= score <= 100:
    print("A")
elif 80 <= score <= 89:
    print("B")
elif 70 <= score <= 79:
    print("C")
elif 60 <= score <= 69:
    print("D")
else:
    print("F")