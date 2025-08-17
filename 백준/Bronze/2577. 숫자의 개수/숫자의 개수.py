import sys

# 세 개의 자연수 A, B, C를 입력받음
A = int(sys.stdin.readline())
B = int(sys.stdin.readline())
C = int(sys.stdin.readline())

# 세 수를 곱하여 결과를 계산
result = A * B * C

# 결과를 문자열로 변환
result_str = str(result)

# 0부터 9까지 각 숫자의 개수를 저장할 리스트를 0으로 초기화
count_list = [0] * 10

# 문자열을 순회하며 각 숫자의 개수를 셈
for char in result_str:
    # 문자를 정수로 변환하여 인덱스로 사용
    digit = int(char)
    # 해당 숫자의 개수를 1 증가
    count_list[digit] += 1

# 각 숫자의 개수를 한 줄에 하나씩 출력
for count in count_list:
    print(count)