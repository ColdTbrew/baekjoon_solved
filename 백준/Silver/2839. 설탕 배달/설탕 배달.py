import sys
input = sys.stdin.readline

N = int(input())
min_bags = -1

# 5kg 봉지를 0개부터 N//5개까지 시도
for x in range(N // 5 + 1):
    remain = N - 5 * x  # 남은 무게
    if remain % 3 == 0:  # 3kg 봉지로 채울 수 있으면
        y = remain // 3  # 3kg 봉지 개수
        bags = x + y     # 총 봉지 개수
        if min_bags == -1 or bags < min_bags:
            min_bags = bags

print(min_bags)