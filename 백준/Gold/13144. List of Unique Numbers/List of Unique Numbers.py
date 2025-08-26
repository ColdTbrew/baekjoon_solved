N = int(input())
array = list(map(int, input().split()))

start = 0
end = 0

visited = [False] * 100_001
# visited = [False] * 6

ans =  0
while start<= end and end < N:
    if not visited[array[end]]:                 # 방문한 적이 없으면 
        visited[array[end]] = True              # 방문했다 표시하고
        end += 1                                # 오른쪽 증가
        ans += (end - start)                     # 경우의수 개산해서 증가
        # print("end 이동   ", visited, "ans ", ans)
    else:                                       # 오른쪽이 방문 했던 숫자이면
        # while visited[array[start]]:            # 방문했던 왼쪽에 기록을
        visited[array[start]] = False       # 방문안한거로 처리하고 왼쪽으로 이동
        start += 1
        # print("start 이동 ", visited, "ans ", ans)

print(ans)