import sys
input = sys.stdin.readline

N = int(input().strip())


cur = 0

def have_6(num):
    num_str = str(num)  # 숫자를 문자열로 변환
    target = "666"      # 찾고자 하는 패턴 (문자열)
    if target in num_str:  # 문자열 안에 "666"이 있는지 확인
        return True
    return False

count = 0
while count<N:
    if have_6(cur):
        count += 1
    cur += 1
print(cur-1)

