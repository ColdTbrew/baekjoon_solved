def check(a, b, total):
    for i in list(a):
        j = total-i
        if j in list(b):
            a.remove(i)
            b.remove(j)
            return True
    return False
            
def solution(coin, cards):
    answer = 1
    n = len(cards) 
    idx = n//3
 
    # 내가 손애 쥐고 시작하는 카드
    my_cards = cards[:n//3]
    print(my_cards)
    leftover = []
    while idx < n:
        leftover.append(cards[idx])
        leftover.append(cards[idx+1])
        idx += 2
        # 손에 쥔 카드로 해결
        if check(my_cards, my_cards, n+1):
            pass
        # 하나만 사고 해결
        elif coin>=1 and check(my_cards, leftover, n+1):
            coin -= 1
            pass
        elif coin >= 2 and check(leftover, leftover, n+1):
            coin -= 2
            pass
        else:
            break
            
        answer += 1
        
        # 모두 산거로 해결
    
    return answer