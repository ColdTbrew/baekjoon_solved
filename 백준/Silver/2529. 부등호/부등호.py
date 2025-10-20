def is_valid(sequence, inequalities):
    """부등호 조건을 만족하는지 확인하는 함수"""
    for i in range(len(inequalities)):
        if inequalities[i] == '<' and sequence[i] >= sequence[i + 1]:
            return False
        if inequalities[i] == '>' and sequence[i] <= sequence[i + 1]:
            return False
    return True

def solve_inequalities(k, inequalities):
    """부등호를 만족하는 최대값과 최소값을 찾는 함수"""
    numbers = list(range(10))  # 0부터 9까지의 숫자
    max_result = None
    min_result = None

    def backtrack(curr_seq, used):
        """백트래킹으로 순열 생성"""
        if len(curr_seq) == k + 1:
            if is_valid(curr_seq, inequalities):
                result = ''.join(map(str, curr_seq))
                nonlocal max_result, min_result
                if max_result is None or result > max_result:
                    max_result = result
                if min_result is None or result < min_result:
                    min_result = result
            return

        for num in numbers:
            if num not in used:
                used.add(num)
                backtrack(curr_seq + [num], used)
                used.remove(num)

    # 초기 호출
    backtrack([], set())
    return max_result, min_result

# 입력 처리
k = int(input())
inequalities = input().split()

# 결과 계산 및 출력
max_val, min_val = solve_inequalities(k, inequalities)
print(max_val)
print(min_val)