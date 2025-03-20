import sys
input = sys.stdin.readline

n = int(input().strip())
s = 0  # 비트마스크: 20비트로 1~20 상태 저장

for _ in range(n):
    cmd_x = input().split()
    cmd = cmd_x[0]
    
    if cmd in ["all", "empty"]:
        if cmd == "all":
            s = (1 << 20) - 1  # 20비트 모두 1: 1~20 포함
        else:
            s = 0  # 공집합
    else:
        x = int(cmd_x[1]) - 1  # 0-based 인덱스 (1~20 → 0~19)
        if cmd == "add":
            s |= (1 << x)  # x번째 비트 1로 설정
        elif cmd == "remove":
            s &= ~(1 << x)  # x번째 비트 0으로 설정
        elif cmd == "check":
            print(1 if (s & (1 << x)) else 0)  # x번째 비트 확인
        elif cmd == "toggle":
            s ^= (1 << x)  # x번째 비트 반전