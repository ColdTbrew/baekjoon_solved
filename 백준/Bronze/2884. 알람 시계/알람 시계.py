H, M = map(int, input().split())

# 45분을 뺍니다.
M -= 45

# 분이 음수일 경우
if M < 0:
    H -= 1
    M += 60

# 시간이 음수일 경우 (자정을 넘어가는 경우)
if H < 0:
    H += 24

print(H, M)