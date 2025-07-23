# 주유소의 리터당 가격이 다름
N = int(input())
distances = list(map(int, input().split()))
prices = list(map(int, input().split()))

total_price = 0 # 총 주유 비용
min_price_so_far = prices[0] # 현재 까지의 가장싼 기름가격

#그리디 알고리즘
for idx in range(0, N-1):
    total_price += distances[idx] * min_price_so_far #idx까지 오는 비용은 연비 * 현재까지의 최소 리터당 가격
    min_price_so_far = min(min_price_so_far, prices[idx+1]) # 현재까지의 최소 리터당 가격 갱신
    
print(total_price)
