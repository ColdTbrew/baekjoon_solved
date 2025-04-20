import sys
input = sys.stdin.readline

# 입력
K, N = map(int, input().split())
have = [int(input()) for _ in range(K)]

# 이분 탐색
def binary_search(arr, target):
    left, right = 1, max(arr)  # 탐색 범위: 1부터 최대 랜선 길이
    result = 0
    
    while left <= right:
        mid = (left + right) // 2  # 현재 길이
        count = sum(x // mid for x in arr)  # 만들 수 있는 랜선 개수
        
        if count >= target:  # N개 이상 만들 수 있으면 길이를 늘려봄
            result = mid  # 가능한 길이 저장
            left = mid + 1
        else:  # N개 미만이면 길이를 줄임
            right = mid - 1
    
    return result

# 출력
print(binary_search(have, N))