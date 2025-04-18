import sys
import heapq

input = sys.stdin.readline

T = int(input().strip())
for _ in range(T):
    k = int(input().strip())
    min_q = []
    max_q = []
    valid = {}  # {값: 개수}로 유효성 추적
    
    for _ in range(k):
        cmd, num = input().split()
        num = int(num)
        
        if cmd == 'I':
            # 삽입: 값만 힙에 추가
            heapq.heappush(min_q, num)
            heapq.heappush(max_q, -num)
            if num in valid:
                valid[num] += 1
            else:
                valid[num] = 1
            
        elif cmd == 'D' and valid:
            if num == 1:  # 최대값 삭제
                # 유효한 최대값 찾기
                while max_q:
                    val = -max_q[0]
                    if val in valid and valid[val] > 0:
                        break
                    heapq.heappop(max_q)
                if max_q:
                    valid[val] -= 1
                    if valid[val] == 0:
                        del valid[val]
                    heapq.heappop(max_q)
            elif num == -1:  # 최소값 삭제
                # 유효한 최소값 찾기
                while min_q:
                    val = min_q[0]
                    if val in valid and valid[val] > 0:
                        break
                    heapq.heappop(min_q)
                if min_q:
                    valid[val] -= 1
                    if valid[val] == 0:
                        del valid[val]
                    heapq.heappop(min_q)
    
    # 유효한 값만 남기기
    while min_q:
        val = min_q[0]
        if val in valid and valid[val] > 0:
            break
        heapq.heappop(min_q)
    while max_q:
        val = -max_q[0]
        if val in valid and valid[val] > 0:
            break
        heapq.heappop(max_q)
    
    # 결과 출력
    if min_q and max_q:
        print(-max_q[0], min_q[0])
    else:
        print("EMPTY")
