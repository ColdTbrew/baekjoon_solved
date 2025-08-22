N = int(input())
# 주식 하나를 산다.
# 원하는 만큼 가지고 있는 주식을 판다.
# 아무것도 안한다.
for _ in range(N):
    day = int(input())
    values = list(map(int, input().split()))
    
    max_earn = 0
    max_price = 0

    for i in range(day-1, -1, -1):
        if values[i] > max_price:
            max_price = values[i]
        else:
            max_earn += max_price - values[i]

    print(max_earn)
    # max price의 Index보다 빠르게 샀으면 max-본인 만큼 얻고 뒤에 샀으면 못얻음