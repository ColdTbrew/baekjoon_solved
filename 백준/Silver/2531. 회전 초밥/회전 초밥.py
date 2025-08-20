N, d, k, c = map(int, input().split())
cho = [int(input()) for _ in range(N)]
#k개를 연속해서 먹으면 
#초밥의 가지수가 d
# 쿠폰 번호는 c
cho_extended = cho + cho[:k]

max_varieties = 0
for i in range(N):
    window = cho_extended[i:i+k]
    
    varieties = set(window)
    
    varieties.add(c)
    
    current_varieties = len(varieties)
    
    if current_varieties > max_varieties:
        max_varieties = current_varieties

print(max_varieties)