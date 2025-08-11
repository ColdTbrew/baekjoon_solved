from itertools import combinations

def get_sums(dices, index, current_sum, sums_count):
    # 재귀적으로 주사위 합계를 계산하는 함수
    if index == len(dices):
        sums_count[current_sum] = sums_count.get(current_sum, 0) + 1
        return

    for val in dices[index]:
        get_sums(dices, index + 1, current_sum + val, sums_count)

def solution(dice):
    n = len(dice)
    max_wins = -1
    answer = []

    # 1. A가 선택할 주사위 조합 구하기
    a_choices = list(combinations(range(n), n // 2))
    # print(a_choices)
    for a_choice_indices in a_choices:
        a_dice_set = [dice[i] for i in a_choice_indices]
        b_choice_indices = [i for i in range(n) if i not in a_choice_indices]
        # print(b_choice_indices)
        b_dice_set = [dice[i] for i in b_choice_indices]
        
        print("aset", a_dice_set)
        print("bset", b_dice_set)
        a_sums = {}
        b_sums = {}

        # 2. 각 조합별 승리 확률 계산 (주사위 합계 경우의 수 구하기)
        get_sums(a_dice_set, 0, 0, a_sums)
        get_sums(b_dice_set, 0, 0, b_sums)
        # print(a_sums)
        # print(b_sums)
        win_count = 0
        for a_sum, a_count in a_sums.items():
            for b_sum, b_count in b_sums.items():
                if a_sum > b_sum:
                    win_count += a_count * b_count

        # 3. 최대 승리 횟수와 조합 저장
        if win_count > max_wins:
            max_wins = win_count
            answer = [i + 1 for i in a_choice_indices]

    return answer