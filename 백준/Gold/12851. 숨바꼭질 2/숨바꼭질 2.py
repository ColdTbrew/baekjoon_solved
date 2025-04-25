import sys
from collections import deque

input = sys.stdin.readline

# 입력 처리
N, K = map(int, input().split())

# 입력 범위 체크
if not (0 <= N <= 100000 and 0 <= K <= 100000):
    print(0)
    print(0)
    sys.exit()

def bfs(start, end):
    # N == K 처리
    if start == end:
        return 0, 1
    # N > K 처리
    if start > end:
        return start - end, 1

    max_range = 100000  # 최대 위치 범위
    q = deque([(start, 0)])  # (위치, 시간)
    dist = [[float('inf'), 0] for _ in range(max_range + 1)]  # [최소 시간, 경로 수]
    dist[start] = [0, 1]  # 시작점: 시간 0, 경로 수 1

    while q:
        cur, time = q.popleft()
        if time > dist[end][0]:  # 최소 시간 초과 시 스킵
            continue

        # 이동: +1, -1, *2
        moves = [cur + 1, cur - 1, cur * 2]
        for new in moves:
            if 0 <= new <= max_range:
                new_time = time + 1
                # 최초 방문
                if dist[new][0] > new_time:
                    dist[new][0] = new_time
                    dist[new][1] = dist[cur][1]
                    q.append((new, new_time))
                # 동일 시간 재방문
                elif dist[new][0] == new_time:
                    dist[new][1] += dist[cur][1]

    # 경로 없음 (문제상 불필요)
    if dist[end][0] == float('inf'):
        return 0, 0
    return dist[end][0], dist[end][1]

# BFS 실행 및 출력
time, count = bfs(N, K)
print(time)
print(count)