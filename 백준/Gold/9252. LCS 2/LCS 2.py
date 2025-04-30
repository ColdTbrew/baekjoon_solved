s1 = input().strip()
s2 = input().strip()

if not s1 or not s2:
    print(0)
else:
    # lcs[i][j] = [길이, 방향] (2=대각선, 1=위, 3=왼쪽)
    lcs = [[[0, -1] for _ in range(len(s2)+1)] for _ in range(len(s1)+1)]
    ans = []
    
    # DP 테이블 채우기
    for i in range(1, len(s1)+1):
        for j in range(1, len(s2)+1):
            if s1[i-1] == s2[j-1]:
                lcs[i][j] = [lcs[i-1][j-1][0] + 1, 2]
            else:
                if lcs[i-1][j][0] >= lcs[i][j-1][0]:
                    lcs[i][j] = [lcs[i-1][j][0], 1]
                else:
                    lcs[i][j] = [lcs[i][j-1][0], 3]
    
    # LCS 문자열 추적
    i, j = len(s1), len(s2)
    while i > 0 and j > 0:
        direction = lcs[i][j][1]
        if direction == 2:
            ans.append(s1[i-1])
            i -= 1
            j -= 1
        elif direction == 1:
            i -= 1
        elif direction == 3:
            j -= 1
    
    # 출력
    lcs_length = lcs[len(s1)][len(s2)][0]
    print(lcs_length)
    if lcs_length > 0:
        print(''.join(ans[::-1]))