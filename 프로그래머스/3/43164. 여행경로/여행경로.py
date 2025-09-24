# 재귀를 사용한 구현
# 인접 리스트가 더 편할듯 

def solution(tickets):
    tics = {}
    for depart, dest in tickets:
        if depart not in tics.keys():
            tics[depart] = [dest]
        else:
            tics[depart].append(dest)
    # 도착지들을 알파벳 순으로정렬
    for depart in tics:
        tics[depart].sort()
    print(tics)
    
    route = []
    
    def dfs(airport ):
        route.append(airport)
        if len(route) == len(tickets) + 1:
            return True
        if airport in tics:
            for i in range(len(tics[airport])):
                if tics[airport][i]: #밸류가 있으면
                    next_airport = tics[airport][i]
                    tics[airport][i] = ""
                    if dfs(next_airport ):
                        return True
                    tics[airport][i] = next_airport 
            #경로가 트루를 못받아오면 이경로로 가면ㅇ나됨 그래서 다음 공항을 다시 제자리에 넣음
        route.pop() # 경로 추가했던거도 다시 빼야함
        return False
            
    dfs("ICN")
    
    
    
    return route
