import sys

def count_moves_to_side(balls, target_color, direction):
    n = len(balls)
    move_count = 0
    start_index = -1

    if direction == 'left':
        # 왼쪽으로 모으는 경우, 오른쪽 끝에서부터 탐색
        i = n - 1
        # 가장 오른쪽 끝에 있는 target_color 볼 무더기는 옮길 필요 없음
        while i >= 0 and balls[i] == target_color:
            i -= 1
        start_index = i
        
        # 나머지 볼 중 target_color 볼의 개수 세기
        for j in range(start_index, -1, -1):
            if balls[j] == target_color:
                move_count += 1
    
    elif direction == 'right':
        # 오른쪽으로 모으는 경우, 왼쪽 끝에서부터 탐색
        i = 0
        # 가장 왼쪽 끝에 있는 target_color 볼 무더기는 옮길 필요 없음
        while i < n and balls[i] == target_color:
            i += 1
        start_index = i
        
        # 나머지 볼 중 target_color 볼의 개수 세기
        for j in range(start_index, n):
            if balls[j] == target_color:
                move_count += 1

    return move_count


n = int(sys.stdin.readline())
balls = sys.stdin.readline().strip()

    
case1 = count_moves_to_side(balls, 'R', 'left')

case2 = count_moves_to_side(balls, 'R', 'right')

case3 = count_moves_to_side(balls, 'B', 'left')

case4 = count_moves_to_side(balls, 'B', 'right')


if 'R' not in balls or 'B' not in balls:
    print(0)
else:
    print(min(case1, case2, case3, case4))
