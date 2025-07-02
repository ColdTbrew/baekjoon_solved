# 입력
N = int(input())  # 스위치 개수
switches = list(map(int, input().split()))  # 스위치 초기 상태
students = int(input())  # 학생 수

# 학생별 조작 처리
for _ in range(students):
    gender, num = map(int, input().split())  # 성별(1:남, 2:여), 받은 수
    
    if gender == 1:  # 남학생
        for i in range(num-1, N, num):  # num의 배수 인덱스 (0-based)
            switches[i] = 1 - switches[i]  # 상태 반전 (0->1, 1->0)
    
    else:  # 여학생
        num -= 1  # 0-based 인덱스로 변환
        left = right = num
        count = 1  # 중심 스위치 포함
        
        # 대칭 확인하며 범위 확장
        while left > 0 and right < N-1 and switches[left-1] == switches[right+1]:
            left -= 1
            right += 1
            count += 2
        
        # 구간 내 스위치 상태 반전
        for i in range(left, right + 1):
            switches[i] = 1 - switches[i]

# 출력
for i in range(0, N, 20):
    print(" ".join(map(str, switches[i:i+20])))