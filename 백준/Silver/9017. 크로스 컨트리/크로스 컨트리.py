from collections import Counter

T = int(input())

for _ in range(T):
    N = int(input())
    scores_input = list(map(int, input().split())) # scores_input으로 변수명 변경

    # 1. 각 팀의 주자 수 계산 (Counter 사용)
    team_counts = Counter(scores_input)

    # 2. 자격을 갖춘 팀 필터링 (6명인 팀)
    # set을 사용하여 빠른 검색 가능
    qualified_teams = {team for team, count in team_counts.items() if count == 6}
    
    # 각 팀의 합산 점수와 5번째 주자 점수를 저장할 딕셔너리 초기화
    # 자격 없는 팀은 아예 딕셔너리에 포함시키지 않음
    team_total_scores = {team: 0 for team in qualified_teams}
    team_runner_counts = {team: 0 for team in qualified_teams} # 각 팀별로 몇 번째 주자인지 카운트
    team_fifth_runner_scores = {team: 0 for team in qualified_teams} # 5번째 주자 점수 (순위) 저장

    current_rank = 1

    for team_id in scores_input:
        if team_id in qualified_teams:
            # 해당 팀의 주자 카운트 증가
            team_runner_counts[team_id] += 1 
            

            if team_runner_counts[team_id] <= 4:
                team_total_scores[team_id] += current_rank
                # print("team id", team_id)
                # print("cur rank", current_rank)
            elif team_runner_counts[team_id] == 5:
                team_fifth_runner_scores[team_id] = current_rank
            current_rank += 1
        

    # 3. 우승팀 결정 로직
    # 최소 합산 점수 초기화
    min_total_score = float('inf')
    # 최소 합산 점수를 가진 팀들을 저장할 리스트 (동점 처리 위함)
    potential_winners = [] 
    # print("team total", team_total_scores)
    for team, total_score in team_total_scores.items():
        if total_score < min_total_score:
            min_total_score = total_score
            potential_winners = [team] # 새로운 최소 점수 발견 시 리스트 초기화
        elif total_score == min_total_score:
            potential_winners.append(team) # 기존 최소 점수와 동일하면 리스트에 추가

    # 4. 동점 처리
    if len(potential_winners) == 1:
        # 단일 우승팀
        print(potential_winners[0])
    else:
        # 여러 팀이 동점일 경우, 5번째 주자의 점수로 비교
        min_fifth_score = float('inf')
        final_winner = -1
        
        for team in potential_winners:
            # 5번째 주자의 점수 확인
            fifth_score = team_fifth_runner_scores[team]
            
            if fifth_score < min_fifth_score:
                min_fifth_score = fifth_score
                final_winner = team
        print(final_winner)