def solution(friends, gifts):
    answer = 0
    table = [[0 for _ in range(len(friends))] for _ in range(len(friends))]
    gift_index = [0] * len(friends)
    answer = [0] * len(friends)

    for gift in gifts:
        give, take = gift.split(" ")
        give_idx, take_idx = friends.index(give), friends.index(take)
        gift_index[give_idx] += 1
        gift_index[take_idx] -= 1
        table[give_idx][take_idx] += 1
        
    for i in range(len(friends)):
        for j in range(i + 1, len(friends)):
            if table[i][j] > table[j][i]:  # i가 준 횟수가 더 많음
                answer[i] += 1
            elif table[i][j] < table[j][i]:  # j가 준 횟수가 더 많음
                answer[j] += 1
            else:
                if gift_index[i] > gift_index[j]:
                    answer[i] += 1
                elif gift_index[i] < gift_index[j]:
                    answer[j] += 1
    print(answer)
    return max(answer)