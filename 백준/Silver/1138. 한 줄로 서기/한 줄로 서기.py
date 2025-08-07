import sys
import heapq
input = sys.stdin.readline

N = int(input())
info = list(map(int, input().split()))
info_with_me = []
for idx, tall_count in enumerate(info):
    info_with_me.append((idx+1, tall_count))

ans = [0] * N
for i in range(N): # 0번 사람부터 도는데
    zcnt = 0
    for j in range(N): #내 앞에 0인 칸의 개수를 셈 0의 개수가 내 앞의 큰사람 수랑 같아지면 넣고 종료
        if zcnt == info[i] and ans[j] == 0:
            ans[j] = i + 1
            break
        elif ans[j] == 0:
            zcnt += 1

print(*ans)