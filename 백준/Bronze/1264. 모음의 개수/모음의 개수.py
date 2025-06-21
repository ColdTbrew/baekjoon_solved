import sys

# 모음 집합 (대소문자 포함)
vowels = set('aeiouAEIOU')

while True:
    # 입력 받기
    line = sys.stdin.readline().rstrip()
    
    # 종료 조건: '#'
    if line == '#':
        break
    
    # 모음 개수 세기
    count = sum(1 for char in line if char in vowels)
    
    # 결과 출력
    print(count)