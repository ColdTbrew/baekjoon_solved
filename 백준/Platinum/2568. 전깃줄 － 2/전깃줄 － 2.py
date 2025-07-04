import sys
from bisect import bisect_left # 리스트에서 특정 값이 들어갈 위치를 빠르게 찾아주는 함수

def solve():
    N = int(sys.stdin.readline()) # 전깃줄의 개수 입력 받기
    wires = []
    for _ in range(N):
        a, b = map(int, sys.stdin.readline().split())
        wires.append((a, b)) # (A 전봇대 번호, B 전봇대 번호) 쌍으로 저장

    # 1. A 전봇대 번호를 기준으로 전깃줄 정렬 📏
    # 이렇게 정렬해야 B 전봇대 번호가 증가하는 순서인지 확인할 수 있어요.
    wires.sort()

    # B 전봇대 번호만 따로 모으기
    b_values = [wire[1] for wire in wires]

    # 2. LIS (최장 증가 부분 수열) 찾기 ✨
    # 'tails'는 가장 긴 증가 부분 수열을 만들기 위한 중요한 도구예요.
    # tails[i]는 길이가 i+1인 증가 부분 수열의 마지막 원소 중 가장 작은 값을 저장해요.
    tails = []
    # 'lis_original_indices'는 tails에 있는 값이 원래 'wires' 리스트의 몇 번째 인덱스였는지 기록해요.
    # 나중에 LIS에 어떤 전깃줄이 포함되었는지 추적할 때 필요해요.
    lis_original_indices = []
    # 'prev_elements_in_lis'는 LIS를 만들 때 각 전깃줄의 바로 앞 전깃줄의 인덱스를 저장해요.
    # LIS 경로를 역추적하는 데 사용돼요.
    prev_elements_in_lis = [-1] * N

    for i in range(N):
        current_b = b_values[i] # 현재 전깃줄의 B 전봇대 번호
        
        # 'tails'에서 current_b가 들어갈 위치 찾기 (이진 탐색)
        # current_b보다 크거나 같은 첫 번째 원소의 인덱스를 찾아줘요.
        idx = bisect_left(tails, current_b)

        if idx == len(tails): # 만약 current_b가 tails의 모든 원소보다 크다면
            tails.append(current_b) # LIS 길이가 늘어남! 새로운 LIS의 끝 원소가 됨
            lis_original_indices.append(i) # 현재 전깃줄의 원래 인덱스 저장
        else: # 그렇지 않다면 (tails 안에 current_b보다 크거나 같은 값이 있다면)
            tails[idx] = current_b # 해당 위치의 값을 current_b로 바꿔치기 (더 작은 값으로 LIS를 이어갈 기회)
            lis_original_indices[idx] = i # 업데이트된 값의 원래 인덱스 저장

        # LIS 경로를 만들기 위해 이전 원소 기록 👣
        if idx > 0:
            prev_elements_in_lis[i] = lis_original_indices[idx - 1]

    # 3. LIS에 포함된 전깃줄 식별하기 (역추적) 🔍
    lis_a_values = set() # LIS에 포함된 A 전봇대 번호들을 저장할 집합
    
    # LIS의 마지막 원소부터 시작해서 역으로 거슬러 올라가요.
    current_idx_in_wires = lis_original_indices[-1]
    while current_idx_in_wires != -1: # -1이 될 때까지 (LIS의 시작점까지)
        lis_a_values.add(wires[current_idx_in_wires][0]) # 해당 전깃줄의 A 번호를 LIS 집합에 추가
        current_idx_in_wires = prev_elements_in_lis[current_idx_in_wires] # 이전 LIS 원소로 이동

    # 4. 제거해야 할 전깃줄 찾아서 출력하기 ✂️
    removed_a_values = []
    for i in range(N):
        # 만약 현재 전깃줄의 A 번호가 LIS 집합에 없다면, 제거해야 할 전깃줄!
        if wires[i][0] not in lis_a_values:
            removed_a_values.append(wires[i][0])

    print(len(removed_a_values)) # 제거해야 할 전깃줄 개수 출력
    for val in removed_a_values:
        print(val) # 제거해야 할 전깃줄의 A 번호 오름차순으로 출력 (이미 wires가 정렬되어 있어서 자연스럽게 오름차순)

# 함수 실행
solve()