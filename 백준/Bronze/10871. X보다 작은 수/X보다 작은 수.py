import sys

def find_smaller_numbers():
    """
    주어진 수열에서 X보다 작은 수들을 찾아 출력합니다.
    """
    try:
        # 첫째 줄에서 N과 X를 입력받습니다.
        N, X = map(int, sys.stdin.readline().split())
        
        # 둘째 줄에서 N개의 정수로 이루어진 수열 A를 입력받습니다.
        A = list(map(int, sys.stdin.readline().split()))
        
        # 결과를 저장할 리스트를 초기화합니다.
        result = []
        
        # 수열 A를 순회하며 X보다 작은 수를 찾습니다.
        for number in A:
            if number < X:
                result.append(number)
        
        # 저장된 결과 리스트의 요소들을 공백으로 구분하여 출력합니다.
        print(*result)
        
    except (IOError, ValueError) as e:
        print(f"입력 오류가 발생했습니다: {e}")

# 함수를 호출하여 프로그램을 실행합니다.
find_smaller_numbers()