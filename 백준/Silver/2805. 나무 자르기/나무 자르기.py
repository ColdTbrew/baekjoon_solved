import sys
input = sys.stdin.readline

N, M = map(int, input().split())
trees = list(map(int, input().split()))

start = 0
end = max(trees)
answer = 0

while start <= end:
    mid = (start + end) // 2
    total = sum(max(0, t - mid) for t in trees)  # 한 줄로 합 계산
    if total >= M:
        answer = mid
        start = mid + 1
    else:
        end = mid - 1

print(answer)