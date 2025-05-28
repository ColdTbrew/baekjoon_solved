import sys
input = sys.stdin.readline

# 입력 처리
S = input().strip()  # 단어 S 입력 (공백 및 개행문자 제거)

# 알파벳 위치를 저장할 배열 (-1로 초기화, a부터 z까지 26개)
alpha = [-1] * 26

# 문자열 S를 순회하며 각 알파벳의 첫 등장 위치 기록
for i in range(len(S)):
    idx = ord(S[i]) - ord('a')  # 문자를 아스키 코드로 변환 후 'a'(97)를 빼서 인덱스(0~25) 계산
    if alpha[idx] == -1:  # 해당 알파벳이 처음 등장한 경우
        alpha[idx] = i

# 결과 출력 (공백으로 구분)
print(' '.join(map(str, alpha)))