import sys
from collections import deque

input = sys.stdin.readline

T = int(input())
for _ in range(T):
    cmds = input().strip()
    N = int(input())
    if N == 0:
        input().strip()  # 빈 배열 입력 소비
        array = deque()
    else:
        array = deque(map(int, input().strip().strip('[]').split(',')))
    
    is_error = False
    r_count = 0  # 뒤집기 횟수
    
    for cmd in cmds:
        if cmd == 'R':
            r_count += 1
        elif cmd == 'D':
            if array:  # 배열이 비어 있지 않으면
                if r_count % 2 == 0:  # 정방향
                    array.popleft()
                else:  # 역방향
                    array.pop()
            else:  # 배열이 비어 있으면 에러
                is_error = True
                break
    
    if is_error:
        print("error")
    else:
        result = list(array)
        if r_count % 2 == 1:  # 홀수 번 뒤집기면 결과 뒤집기
            result.reverse()
        print(f"[{','.join(map(str, result))}]")