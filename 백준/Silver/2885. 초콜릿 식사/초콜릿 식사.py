import sys

K = int(input())

# for smallest in range(K, 1_000_000):

#K보다 작은 가장 작은 초콜릿 크기
size = 1
while size < K:
    size = size << 1
    # 두배씩 커지면서 K보다 작은 size
# print(size)
ans1 = size
# 쪼개는 횟수세기
count = 0
while K > 0:
    if K >= size: # size가 k 보다 작아지면 고를 수 있으니까 
        K -= size # k 개를 먹어야해서 작아진 사이즈만큼 할당량 채움
    else:
        size //= 2 #k 보다 size가 큰 경우, 즉 안쪼갠 상태.  반으로 쪼갬
        count += 1 

print(ans1, count)
# 8  4  2 
# 안쪼갬   8
# 1번 쪼갬 4 4 <- 6개 먹기 불가능
# 2번 쪼갬 2 2 4 <- 6개 먹기 가능

