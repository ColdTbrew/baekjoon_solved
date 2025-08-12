import sys
from collections import deque

N, K = map(int, input().split())
array = list(map(int, input().split()))

#같은 원소가 k 개 이하인 최장 연속 부분 수열

# 같은 원소의 개수를 세면서 투포인터를 활용해 탐색하자
i, j = 0, 0
lcs =  0
from collections import defaultdict
count_dic = defaultdict(int)

while j < N:
    
    count_dic[array[j]] += 1

    # 딕셔너리에 모든 value 값이 k 이하로 만들고 
    # k개 이상인게 있다면 그 숫자 위치부터 다시 시작ㄴ
    while count_dic[array[j]] > K:
        count_dic[array[i]] -= 1
        # print("erase")
        i += 1
    

    lcs = max(lcs, j-i+1)
    # print("count_dic", count_dic)
    # print("lcs", lcs)
    j += 1

print(lcs)

