N, X = map(int, input().split())
visits = list(map(int, input().split()))

# 연속된 x일 동안 가장 많이 들어온 방문자 수

visit_sum = sum(visits[0:X])
max_visits_sum = visit_sum
max_visits_sum_count = 1
for idx in range(X, N):
    visit_sum += visits[idx] # 새로운 인덱스를 더하고
    visit_sum -= visits[idx-X] # 왼쪽 가장자리 빼고
    
    if visit_sum > max_visits_sum:
        max_visits_sum = visit_sum
        max_visits_sum_count = 1
    elif visit_sum == max_visits_sum:
        max_visits_sum_count += 1


if max_visits_sum == 0:
    print("SAD")
else:
    print(max_visits_sum)
    print(max_visits_sum_count)
