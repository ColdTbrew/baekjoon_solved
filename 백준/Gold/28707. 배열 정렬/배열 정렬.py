import sys
from heapq import heappop, heappush

# 빠르게 입력 받기
input = sys.stdin.readline

# 1. 입력 받기
N = int(input())  # 배열의 길이
# 배열을 문자열로 변환 (숫자를 1씩 빼서 0~9 범위로)
A = ''
for number in input().split():
    A += str(int(number) - 1)
M = int(input())  # 조작의 개수
# 조작 정보 (l, r, c) 리스트로 저장
operations = []
for _ in range(M):
    l, r, c = map(int, input().split())  # l, r은 1-based, c는 비용
    operations.append((l - 1, r - 1, c))  # 0-based 인덱스로 변환

# 2. 다익스트라를 위한 초기 설정
# 우선순위 큐: (비용, 현재 배열 상태)
priority_queue = [(0, A)]
# 각 배열 상태별 최소 비용을 저장하는 딕셔너리
min_costs = {A: 0}  # 초기 상태 비용은 0

# 3. 다익스트라 알고리즘으로 최소 비용 탐색
while priority_queue:
    # 가장 비용이 작은 상태를 꺼냄
    current_cost, current_state = heappop(priority_queue)
    
    # 이미 더 저렴한 경로가 있다면 스킵
    if min_costs[current_state] < current_cost:
        continue
    
    # 모든 가능한 조작을 하나씩 적용
    for left, right, cost in operations:
        # 새 배열 상태 만들기: left-1과 right-1 위치를 교환
        new_state = (current_state[:left] + 
                     current_state[right] + 
                     current_state[left + 1:right] + 
                     current_state[left] + 
                     current_state[right + 1:])
        
        # 새 상태가 더 저렴하거나 처음이라면 업데이트
        if new_state not in min_costs or min_costs[new_state] > current_cost + cost:
            min_costs[new_state] = current_cost + cost
            heappush(priority_queue, (current_cost + cost, new_state))

# 4. 결과 확인
# 정렬된 상태 만들기 (예: "0432" → "0123")
sorted_state = ''.join(sorted(A))
# 정렬된 상태에 도달 가능한지 확인
if sorted_state not in min_costs:
    print(-1)  # 불가능하면 -1 출력
else:
    print(min_costs[sorted_state])  # 최소 비용 출력