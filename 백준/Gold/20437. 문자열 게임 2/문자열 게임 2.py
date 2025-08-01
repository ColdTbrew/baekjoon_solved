t = int(input())

for _ in range(t):
    word = str(input().strip())
    K = int(input())
    memo = [[] for _ in range(27)]

    result = []

    for num in range(len(word)):
        alpha = ord(word[num]) - ord('a')
        memo[alpha].append(num)
        if len(memo[alpha]) >= K: #그 알파벳이 K 개 이상있다면
            #가능한 결과 저장
            result.append(
                # 뒤에서 k번째 알파벳의 위치부터 마지막 번째 위치까지의 워드의 슬라이스를  저장함
                word[memo[alpha][-K]:memo[alpha][-1] + 1]
            )
    if len(result) == 0:
        print(-1)
    else:
        result.sort(key = lambda x: len(x))
        print(len(result[0]), len(result[-1]))