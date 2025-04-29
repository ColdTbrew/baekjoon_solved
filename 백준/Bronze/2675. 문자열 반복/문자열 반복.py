# 테스트 케이스 개수 T 입력
T = int(input())

# 각 테스트 케이스 처리
for _ in range(T):
    # R과 S 입력 (공백으로 구분)
    R, S = input().split()
    R = int(R)  # 반복 횟수 R을 정수로 변환
    
    # 결과 문자열 P 생성
    P = ''
    for char in S:
        P += char * R  # 각 문자를 R번 반복하여 P에 추가
    
    # 결과 출력
    print(P)