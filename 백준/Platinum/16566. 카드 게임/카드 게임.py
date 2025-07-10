import bisect

# 입력 처리
N, M, K = map(int, input().split())
minsoo_cards = list(map(int, input().split()))
cheolsu_cards = list(map(int, input().split()))

# 민수의 카드를 정렬
minsoo_cards.sort()

# 사용한 카드를 추적하기 위한 플래그 배열
used = [False] * M

# 결과 저장 리스트
result = []

# 각 라운드에서 철수의 카드 처리
for cheolsu_card in cheolsu_cards:
    # 철수의 카드보다 큰 민수의 카드 중 가장 작은 카드의 인덱스 찾기
    idx = bisect.bisect_right(minsoo_cards, cheolsu_card)
    
    # 사용되지 않은 카드 중 가장 왼쪽의 카드 찾기
    while idx < M and used[idx]:
        idx += 1
    
    # 유효한 카드가 있는 경우
    if idx < M:
        used[idx] = True  # 카드 사용 표시
        result.append(minsoo_cards[idx])
    else:
        # 사용 가능한 카드가 없으면, 사용되지 않은 가장 작은 카드 선택
        for i in range(M):
            if not used[i]:
                used[i] = True
                result.append(minsoo_cards[i])
                break

# 결과 출력
for card in result:
    print(card)