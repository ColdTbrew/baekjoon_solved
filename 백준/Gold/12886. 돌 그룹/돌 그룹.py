from collections import deque

def solution(A, B, C):
    S = A + B + C
    if S % 3 != 0:
        return 0  # 총합이 3의 배수가 아니면 절대 같아질 수 없음

    visited = [[False] * 1501 for _ in range(1501)]  # A,B 최대 1500까지 고려
    q = deque()

    # 초기 상태 정렬
    stones = sorted([A, B, C])
    a, b, c = stones
    q.append((a, b))
    visited[a][b] = True

    while q:
        x, y = q.popleft()
        z = S - x - y
        # 세 그룹이 같으면 성공
        if x == y == z:
            return 1

        # 세 그룹 중 두 개를 선택해 연산
        for a, b in ((x, y), (x, z), (y, z)):
            if a == b:  # 같으면 패스 (연산 정의상 다를 때만)
                continue
            if a < b:
                na = a * 2
                nb = b - a
            else:
                na = a - b
                nb = b * 2

            # 나머지 하나 계산 후 정렬
            nc = S - na - nb
            nxt = sorted([na, nb, nc])
            nx, ny = nxt[0], nxt[1]

            if not visited[nx][ny]:
                visited[nx][ny] = True
                q.append((nx, ny))
    return 0

A, B, C = map(int, input().split())
print(solution(A, B, C))