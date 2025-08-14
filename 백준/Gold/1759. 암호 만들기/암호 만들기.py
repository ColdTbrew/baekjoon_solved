L, C = map(int, input().split())
hubo = list(input().strip().split())

hubo.sort()
# print(hubo)


# 길이가 L
# hubo를 정렬한다음에 하나씩 넣어가면서 길ㅇ이가 444444444가 되ㅣㅣㅣㅣㅣㅣㅣㅣㅣㅣ면 출력하기

ans = []
#최소 한 개의 모음(a, e, i, o, u)과 최소 두 개의 자음
def dfs(index, curans):
    if len(curans) == L: #길이가 됨
        # print("조합 찾음", "idx : ", index, "curans", curans)
        mo_count = 0
        
        mo_count += curans.count('a')
        mo_count += curans.count('e')
        mo_count += curans.count('i')
        mo_count += curans.count('o')
        mo_count += curans.count('u')
    
        ja_count = len(curans) - mo_count
        if mo_count < 1 or ja_count < 2:
            return
        ans.append("".join(curans))
        return

    #길이가 넘지 않으면
    for i in range(index, C):
        # print("index : ",/ index, "i+1:", i+1)
        dfs(i+1, curans + [hubo[i]])



dfs(0, [])

print(*ans, sep= "\n")