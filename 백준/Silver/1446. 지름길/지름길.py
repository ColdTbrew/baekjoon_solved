import sys

N, D = map(int, input().split())
# 지름길 딕셔너리
shortcuts = {}
for _ in range(N):
    start, end, length = map(int, sys.stdin.readline().split())
    if end <= D and end - start > length:
        if end not in shortcuts:
            shortcuts[end] = []
        shortcuts[end].append((start, length))

# print(shortcuts)

# dp 배열을 선언해 한칸씩 가면서 i 길이 만큼 가는데 사용된 최소 비용 갱신
dp = [i for i in range(0, D+1)]
for i in range(1, D+1):
    dp[i] = dp[i-1] + 1 # 기본 케이스

    # 만약 i 가 shortcut end 에 포함된다면 dp[end] + cost
    if i in shortcuts:
        for start, length in shortcuts[i]:
            dist_via_shortcut = dp[start] + length
            dp[i] = min(dp[i], dist_via_shortcut)
            # print("dp[",i,"] " , dp[i])

print(dp[D])