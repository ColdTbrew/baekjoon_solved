def w(a, b, c):
    # 메모이제이션 배열: 0부터 20까지의 범위만 저장
    if a <= 0 or b <= 0 or c <= 0:
        return 1
    if a > 20 or b > 20 or c > 20:
        return w(20, 20, 20)
    
    # 메모이제이션 확인
    if dp[a][b][c] != -1:
        return dp[a][b][c]
    
    # 조건에 따른 재귀 계산
    if a < b and b < c:
        dp[a][b][c] = w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c)
    else:
        dp[a][b][c] = w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1)
    
    return dp[a][b][c]

# 메모이제이션 배열 초기화 (0~20 범위, -1로 초기화)
dp = [[[-1] * 21 for _ in range(21)] for _ in range(21)]

# 입력 처리
while True:
    a, b, c = map(int, input().split())
    if a == -1 and b == -1 and c == -1:
        break
    print(f"w({a}, {b}, {c}) = {w(a, b, c)}")