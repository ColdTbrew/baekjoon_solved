import sys
input = sys.stdin.readline


#그 다음, 수의 등장 횟수가 커지는 순으로, 그러한 것이 여러가지면 수가 커지는 순으로 정렬한다.
r, c, k = map(int, input().split())

grid = []
for i in range(3):
    row = list(map(int, input().split()))
    grid.append(row)

# print(grid)
from collections import Counter

def sort_by_count(array):
    count = Counter(array)
    sorted_array = []
    for key in count:
        if key != 0:
            sorted_array.append((key, count[key]))
    sorted_array.sort(key = lambda x: (x[1], x[0]))
    done = []
    for s0, s1 in sorted_array:
        done.append(s0)
        done.append(s1)
    return done


def row(grid):
    # 모든 행에 대해서 정렬을 수행한다
    new_grid = [[] for _ in range(len(grid))] # 가장 큰 열기준으로 
    max_len = 0
    for i in range(len(grid)):
        new_grid[i] = sort_by_count(grid[i])
        max_len = max(len(new_grid[i]), max_len)
    for i in range(len(grid)):
        if len(new_grid[i]) < max_len:
            new_grid[i].extend([0] * (max_len - len(new_grid[i])))

    return new_grid

def col(grid):
    max_len = 0
    cols = []
    for j in range(len(grid[0])): # 모든 열에 대해서 
        col = [row[j] for row in grid] # 모든 row의 j번째 열의 값을 가져옴
        new_col = sort_by_count(col)
        cols.append(new_col)
        max_len = max(len(new_col), max_len)
    for i in range(len(cols)):
        if len(cols[i]) < max_len:
            cols[i].extend([0] * (max_len - len(cols[i])))
    
    new_grid = [[0]*len(cols) for _ in range(len(cols[0]))]
    # print(*cols, sep= '\n')
    # print("---------")
    for i in range(len(cols[0])):
        for j in range(len(cols)):
            new_grid[i][j] = cols[j][i]
    
    return new_grid

for time in range(0, 101):
    if r-1 < len(grid) and c-1< len(grid[0]) and grid[r-1][c-1] == k:
        print(time)
        break
    if len(grid) >= len(grid[0]): # 행이 더 길거나 같으면
        grid = row(grid)
    else:
        grid = col(grid)
    if time == 100:
        print(-1)
        break

# def transpose(grid):
#     for r in range(len(grid)):
#         for c in range(len(grid[0])):
#             if r > c:
#                 grid[r][c], grid[c][r] = grid[c][r], grid[r][c]
#     return grid