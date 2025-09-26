from collections import defaultdict
def solution(arrows):
    answer = 0
    visit = defaultdict(list)
    x,y = 0,0
    dx,dy = [0,1,1,1,0,-1,-1,-1],[1,1,0,-1,-1,-1,0,1]

    for arrow in arrows:
        for _ in range(2):              # 대각선 판별을 위해 2씩
            nx = x + dx[arrow]
            ny = y + dy[arrow]  
            if (nx,ny) in visit and (x,y) not in visit[(nx,ny)]:    # 방문했던 점이지만 경로가 겹치지 않는 경우, 방+1
                answer += 1
                visit[(x,y)].append((nx,ny))
                visit[(nx,ny)].append((x,y))
            elif (nx,ny) not in visit:                  # 방문하지 않았던 경우
                visit[(x,y)].append((nx,ny))            # 경로가 겹치는 경우는 따로 해줄 필요 없음
                visit[(nx,ny)].append((x,y))
            x,y = nx, ny        # 이동
    return answer