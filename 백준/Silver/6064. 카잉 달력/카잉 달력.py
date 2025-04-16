T = int(input())

for _ in range(T):
    M, N, x, y = map(int, input().split())
    answer = -1
    candidate = x  # candidate는 항상 x + k*M 형태임.
    
    # candidate가 M*N을 넘어서기 전까지 반복 (최악의 경우 M*N 해까지 확인)
    while candidate <= M * N:
        # candidate가 N에 대해 올바른 해인지 확인
        # 문제에서 y가 N이면 candidate % N == 0이 되어야 하므로, (candidate - y) % N == 0 조건을 사용
        if (candidate - y) % N == 0:
            answer = candidate
            break
        candidate += M
    
    print(answer)