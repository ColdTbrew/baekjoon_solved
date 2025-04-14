from collections import Counter
import sys
input = sys.stdin.readline

# 입력 처리
N = int(input())
fruit = list(map(int, input().split()))

# 슬라이딩 윈도우 초기화
left = 0
max_length = 0
fruit_counter = Counter()

# 오른쪽 포인터로 윈도우 확장
for right in range(N):
    # 현재 과일 추가
    fruit_counter[fruit[right]] += 1
    
    # 과일 종류가 2개 초과 시 윈도우 축소
    while len(fruit_counter) > 2:
        fruit_counter[fruit[left]] -= 1
        if fruit_counter[fruit[left]] == 0:
            del fruit_counter[fruit[left]]
        left += 1
    
    # 최대 길이 갱신
    max_length = max(max_length, right - left + 1)

# 결과 출력
print(max_length)