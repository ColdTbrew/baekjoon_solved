import math
def solution(n, bans):
    answer = ''
    table = {}
    for idx, value in enumerate(list("abcdefghijklmnopqrstuvwxyz"), 1): # 인덱스를 1부터 생성해라
        table[value] = idx
    # print(table)
    bans = sorted(bans, key = lambda x: (len(x), x)) # 길이로 먼저 정렬, 그다음 알파벳 순서로
    # print(bans)
    
    actual_number = n # 찾아야할 숫자의 번호
    for string in bans:
        # 현재 문자열 'string'을 뒤집어서 리스트로 만듭니다. (26진법 계산을 용이하게 하기 위함)
        string_list = list(reversed(string))
        number = 0
        # 문자열의 길이만큼 반복하며, 각 자릿수(idx)에 대한 값을 계산합니다.
        for idx in range(len(string)):
            # 26의 거듭제곱에 해당 알파벳의 번호를 곱하여 10진수 값을 계산하고 'number'에 더합니다.
            # print(string_list[idx])
            number += (math.pow(26, idx) * table[string_list[idx]])
        if number > actual_number: # 계산된 10진수 값이 actual_number 보다 크면 다음 문자열을 확인할 필요가 없음
            break
        actual_number += 1
        
    n_26 = []
    while actual_number> 0:
        share = actual_number // 26
        remainer = actual_number % 26
        if remainer == 0:
            remainer = 26
            share -= 1
        n_26.append(remainer)
        actual_number = share
    # print(n_26)
    n_26.reverse()
    alphabets = list("abcdefghijklmnopqrstuvwxyz")
    answer = []
    for value in n_26:
        answer.append(alphabets[value-1])
    return "".join(answer)