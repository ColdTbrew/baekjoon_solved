# i 번째 공장에서 정확하게 Ai개의 라면을 구매하는 최소비용
N = int(input())
ramen = list(map(int, input().split()))

total_price = 0 # 총 구매

ramen.extend([0, 0])

#그리디 알고리즘
for idx in range(0, N):
    if ramen[idx] > 0:
        # 스페셜 2개 묶음
        if ramen[idx+1] > ramen[idx+2]:
            buy_two = min(ramen[idx], ramen[idx+1] - ramen[idx+2])
            total_price += buy_two * 5
            ramen[idx] -= buy_two
            ramen[idx+1] -= buy_two
    
        # 최대 이익인 3개 묶음 시도
        buy_three = min(ramen[idx], ramen[idx+1], ramen[idx+2])
        total_price += buy_three * 7
        ramen[idx] -= buy_three
        ramen[idx+1] -= buy_three
        ramen[idx+2] -= buy_three

        
        # 두개 묶음 시도
        buy_two = min(ramen[idx], ramen[idx+1])
        total_price += buy_two * 5
        ramen[idx] -= buy_two
        ramen[idx+1] -= buy_two

        # 마지막 1개 시도
        total_price += ramen[idx] * 3
    
print(total_price)
