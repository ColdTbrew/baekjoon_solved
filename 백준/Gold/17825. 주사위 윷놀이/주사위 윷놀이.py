graph = [
    [1], [2], [3], [4], [5], [6, 21],
    [7], [8], [9], [10], [11, 25],
    [12], [13], [14], [15], [16, 27],
    [17], [18], [19], [20], [32],
    [22], [23], [24], [30], [26], [24], [28],[29],[24], [31],[20], [32]
]
score = [
    0, 2, 4, 6, 8, 
    10, 12,14, 16,18,
    20,22,24,26,28,
    30,32,34,36,38,
    40,13,16,19,25,
    22,24,28,27,26,
    30,35,0
]

ans = 0
dice = list(map(int, input().split()))

def bt(depth, result, horse):
    global ans
    if depth == 10: #10번의 턴이 지나면
        ans = max(ans, result)
        return
    for i in range(4): # 4개의 말에 대해서
        x = horse[i]

        if len(graph[x]) == 2: #  두갈래 가능이면 무조건 파란 화살표로
            x = graph[x][1] # 두번째 갈래길가는놈
        else:
            x = graph[x][0]
        for _ in range(1, dice[depth]): # 한칸 이동했으니까 dice에 적힌수 - 1만큼 앞으로 가기
            x = graph[x][0] 

        if x == 32 or ( x< 32 and x not in horse):
            before = horse[i] #이전 말의 위치
            horse[i] = x # 현재 말 위치  갱신
            bt(depth+1, result + score[x] , horse)

            horse[i] = before # i 번째 말 되돌려주기

bt(0, 0, [0, 0, 0, 0])
print(ans)