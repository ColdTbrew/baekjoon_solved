import sys
input = sys.stdin.readline

# 입력 처리
N, M, K = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]

# 양분 초기화 (모든 칸에 초기 양분 5)
fertilizer = [[5] * N for _ in range(N)]
# 나무 정보 초기화 (각 칸에 나무 나이 리스트)
trees = [[[] for _ in range(N)] for _ in range(N)]

# 나무 입력 (1-based -> 0-based로 변환)
for _ in range(M):
    x, y, z = map(int, input().split())
    trees[x-1][y-1].append(z)

def spring():
    deads = []
    for r in range(N):
        for c in range(N):
            if trees[r][c]:
                # 나이가 어린 순으로 정렬
                trees[r][c].sort()
                new_trees = []
                for age in trees[r][c]:
                    if fertilizer[r][c] >= age:
                        fertilizer[r][c] -= age
                        new_trees.append(age + 1)  # 나이 증가
                    else:
                        deads.append((r, c, age))  # 죽은 나무
                trees[r][c] = new_trees
    return deads

def summer(deads):
    for r, c, age in deads:
        fertilizer[r][c] += age // 2  # 죽은 나무의 나이 // 2 만큼 양분 추가

def autumn():
    directions = [(-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1)]
    for r in range(N):
        for c in range(N):
            for age in trees[r][c]:
                if age % 5 == 0:
                    for dr, dc in directions:
                        nr, nc = r + dr, c + dc
                        if 0 <= nr < N and 0 <= nc < N:
                            trees[nr][nc].append(1)  # 나이 1인 나무 추가

def winter():
    for r in range(N):
        for c in range(N):
            fertilizer[r][c] += A[r][c]  # 양분 추가

def simulate():
    for _ in range(K):
        deads = spring()  # 봄
        summer(deads)     # 여름
        autumn()          # 가을
        winter()          # 겨울
    # 살아있는 나무 개수 세기
    return sum(len(trees[r][c]) for r in range(N) for c in range(N))

if __name__ == "__main__":
    result = simulate()
    print(result)