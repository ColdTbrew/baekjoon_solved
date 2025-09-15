def solution(players, m, k):
    answer = 0
    table = []
    cur_user = 0
    cur_server = []
    
    total_count = 0
    for time in range(24):
        count = 0
        while players[time] >= m*(len(cur_server)+1):
            cur_server.append(time)
            count += 1
        table.append([players[time], len(cur_server), count])
        cur_server.sort(reverse = True)
        # print(cur_server)
        while cur_server and cur_server[-1] + k <= time + 1:
            cur_server.pop()
            
        total_count += count
    # print(table)
    return total_count