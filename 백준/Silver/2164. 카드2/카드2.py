n = int(input())
# candi = list(map(int, input().split()))

from collections import deque


cards = deque(range(1,n+1))
# print(cards)
while len(cards) > 1:  # 1개 남을 때까지 반복
    cards.popleft()    # 첫 번째 카드 버리기
    if len(cards) > 1: # 아직 1개 이상 남았으면 옮기기
        cards.append(cards.popleft())

print(cards[0])