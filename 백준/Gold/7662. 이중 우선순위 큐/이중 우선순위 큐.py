import sys
from collections import deque
import heapq

input = sys.stdin.readline

T = int(input().strip())
for _ in range(T):
    k = int(input().strip())
    min_q = []
    max_q = []
    valid = {}  # 값의 유효성 추적: {값: 개수}
    
    for i in range(k):
        cmd, num = input().split()
        num = int(num)
        
        if cmd == 'I':
            # 삽입: min_q와 max_q에 추가, valid 업데이트
            heapq.heappush(min_q, (num, i))  # (값, 삽입 순서)
            heapq.heappush(max_q, (-num, i))  # (-값, 삽입 순서)
            valid[num] = valid.get(num, 0) + 1
            
        elif cmd == 'D' and valid:
            if num == 1:  # 최대값 삭제
                # max_q에서 유효한 최대값 찾기
                while max_q and valid.get(-max_q[0][0], 0) == 0:
                    heapq.heappop(max_q)
                if max_q:
                    val, _ = max_q[0]
                    valid[-val] -= 1
                    heapq.heappop(max_q)
            elif num == -1:  # 최소값 삭제
                # min_q에서 유효한 최소값 찾기
                while min_q and valid.get(min_q[0][0], 0) == 0:
                    heapq.heappop(min_q)
                if min_q:
                    val, _ = min_q[0]
                    valid[val] -= 1
                    heapq.heappop(min_q)
    
    # 최종 결과 계산: 유효한 값만 추출
    while min_q and valid.get(min_q[0][0], 0) == 0:
        heapq.heappop(min_q)
    while max_q and valid.get(-max_q[0][0], 0) == 0:
        heapq.heappop(max_q)
    
    if min_q and max_q:
        max_val = -max_q[0][0]
        min_val = min_q[0][0]
        print(max_val, min_val)
    else:
        print("EMPTY")