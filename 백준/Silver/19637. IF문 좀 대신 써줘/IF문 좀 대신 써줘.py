import sys
import bisect
read_input = sys.stdin.readline

N, M = map(int, read_input().split())


# 등급 기준 입력
board = []
for _ in range(N):
    name, power_min = read_input().strip().split()
    board.append((name, int(power_min)))
    

power_mins_only = [item[1] for item in board]

def find_title(current_power):
    idx = bisect.bisect_left(power_mins_only, current_power)
    if idx == N:
        return board[N-1][0]
    # 그 외의 경우 (idx가 0부터 N-1 사이일 때),
    # 해당 인덱스에 해당하는 칭호가 current_power로 얻을 수 있는 칭호입니다.
    else:
        return board[idx][0]

# 쿼리 처리
for _ in range(M):
    power_query = int(read_input())
    print(find_title(power_query))
    