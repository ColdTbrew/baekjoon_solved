# 연도를 입력받음
year = int(input())

# 윤년 조건:
# 1. 4의 배수이면서 100의 배수가 아닌 경우 -> 윤년
# 2. 400의 배수인 경우 -> 윤년
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(1)  # 윤년이면 1 출력
else:
    print(0)  # 윤년이 아니면 0 출력