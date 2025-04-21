import sys
input = sys.stdin.readline

# 세 문자열 입력
s1 = input().strip()
s2 = input().strip()
s3 = input().strip()

# s3를 기준으로 i+2 추정
if s3.isdigit():
    # s3가 숫자인 경우
    n = int(s3)
elif s3 == "Fizz":
    # s3가 Fizz면 i+2는 3의 배수
    if s2.isdigit():
        n = int(s2) + 1  # s2 = i+1, s3 = i+2
    elif s1.isdigit():
        n = int(s1) + 2
    else:
        n = 3  # 최소 3의 배수
elif s3 == "Buzz":
    # s3가 Buzz면 i+2는 5의 배수
    if s2.isdigit():
        n = int(s2) + 1
    elif s1.isdigit():
        n = int(s1) + 2
    else:
        n = 5  # 최소 5의 배수
else:  # s3 == "FizzBuzz"
    # s3가 FizzBuzz면 i+2는 15의 배수
    if s2.isdigit():
        n = int(s2) + 1  # s2 = i+1, s3 = i+2
    elif s1.isdigit():
        n = int(s1) + 2
    else:
        n = 15  # 최소 15의 배수

# i+3 계산
n += 1  # i+2 -> i+3

# i+3에 대해 FizzBuzz 규칙 적용
if n % 3 == 0 and n % 5 == 0:
    print("FizzBuzz")
elif n % 3 == 0:
    print("Fizz")
elif n % 5 == 0:
    print("Buzz")
else:
    print(n)