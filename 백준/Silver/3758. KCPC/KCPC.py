import sys

def solve():
    n, k, t, m = map(int, sys.stdin.readline().split())

    # scores[i][j]: i팀이 j번 문제에서 얻은 최고 점수
    scores = [[0 for _ in range(k + 1)] for _ in range(n + 1)]
    # submit_count[i]: i팀의 총 제출 횟수
    submit_count = [0 for _ in range(n + 1)]
    # last_submit_time[i]: i팀의 마지막 제출 시간
    last_submit_time = [0 for _ in range(n + 1)]

    for time in range(m):
        team_id, problem_id, score = map(int, sys.stdin.readline().split())

        # 해당 문제의 최고 점수만 갱신
        if score > scores[team_id][problem_id]:
            scores[team_id][problem_id] = score
        
        # 제출 횟수 증가
        submit_count[team_id] += 1
        
        # 마지막 제출 시간 갱신
        last_submit_time[team_id] = time + 1

    final_scores = []
    for team_id in range(1, n + 1):
        total_score = sum(scores[team_id])
        final_scores.append((total_score, submit_count[team_id], last_submit_time[team_id], team_id))

    # 정렬: 1. 총점 내림차순, 2. 제출 횟수 오름차순, 3. 마지막 제출 시간 오름차순
    final_scores.sort(key=lambda x: (-x[0], x[1], x[2]))
    
    # 당신 팀의 순위 찾기
    for rank, score_info in enumerate(final_scores):
        if score_info[3] == t:
            print(rank + 1)
            return

T = int(sys.stdin.readline())
for _ in range(T):
    solve()