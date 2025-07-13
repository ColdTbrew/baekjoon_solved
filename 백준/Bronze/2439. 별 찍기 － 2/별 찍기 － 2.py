# 입력: N을 받음 (1 ≤ N ≤ 100)
N = int(input())

# 1부터 N까지 반복
for i in range(1, N + 1):
    # 공백: N-i개 출력 (오른쪽 정렬을 위해)
    print(" " * (N - i), end="")
    # 별: i개 출력
    print("*" * i)