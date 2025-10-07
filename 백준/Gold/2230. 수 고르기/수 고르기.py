# A 수열을 정렬후에 투포인터를 이용해서
# i는 0부터 N-1까지 순회하면서
# j는 만약 A[j]-A[i]가 M보다 작으면 j를 늘리고 M이상 차이난다면 최소 차이 갱신하고 i를 증가시키자

N, M = map(int, input().split())
A = []
for _ in range(N):
    A.append(int(input()))

A.sort()

j = 0
min_diff = float('inf')
for i in range(N):
    while j < N and A[j] - A[i] < M:
        j += 1
    if j < N:
        min_diff = min(min_diff,A[j] - A[i])
    # print(f"i={i}, j={j}, diff={A[j] - A[i] if j < N else 'N/A'}")  # 디버깅용

print(min_diff)