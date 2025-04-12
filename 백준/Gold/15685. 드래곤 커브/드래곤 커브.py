import sys
input = sys.stdin.readline

# 입력 처리
N = int(input())
grid = [[0] * 101 for _ in range(101)]

# 방향: 0(→), 1(↑), 2(←), 3(↓)
dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

def make_curve(x, y, d, g):
    # 방향 리스트 초기화 (0세대)
    dirs = [d]
    # g세대까지 방향 생성
    for _ in range(g):
        # 이전 세대 역순으로 90도 회전 (dir + 1)
        for dir in reversed(dirs):
            dirs += [(dir+1)%4]
        # dirs += [(dir + 1) % 4 for dir in reversed(dirs)]
    # print("\ndirs: ", dirs)
    # 격자에 커브 표시
    grid[y][x] = 1
    for dir in dirs:
        x += dx[dir]
        y += dy[dir]
        grid[y][x] = 1
        # print("final xy", x, y)

def count_dragon_curve():
    count = 0
    for i in range(100):
        for j in range(100):
            if (grid[i][j] == 1 and
                grid[i][j+1] == 1 and
                grid[i+1][j] == 1 and
                grid[i+1][j+1] == 1):
                count += 1
    return count

# 드래곤 커브 생성
for _ in range(N):
    x, y, d, g = map(int, input().split())
    make_curve(x, y, d, g)

# 정사각형 개수 출력
print(count_dragon_curve())