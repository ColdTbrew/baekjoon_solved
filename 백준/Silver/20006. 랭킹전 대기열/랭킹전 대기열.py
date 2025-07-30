import sys
input = sys.stdin.readline

p, m = map(int, input().split())
rooms = []
for _ in range(p):
    level, name = input().split()
    level = int(level)
    if len(rooms) == 0: # 방이 없다면 새로운 방 생성후 입장
        rooms.append([level, [(level,name)]])
    else: # 방이 있음
        # 입장 가능한 방이 있음
        # 입장 후 대기한다
        is_entered = False
        for idx in range(len(rooms)):
            origin_level, team_list = rooms[idx]
            if origin_level-10 <= level <= origin_level + 10 and len(team_list) < m:
                rooms[idx][1].append((level,name))
                is_entered = True
                break
        # 입장 가능한 방이 없음
        if not is_entered:
            rooms.append([level, [(level,name)]]) # 본인이 처음으로 그룸 들어감
            

# print(rooms)
for idx in range(len(rooms)):
    rooms[idx][1].sort(key = lambda x: x[1])
    if len(rooms[idx][1]) == m:
        print("Started!")
    else:
        print("Waiting!")
    for tup in rooms[idx][1]:
        print(tup[0], tup[1])
