def solution(bandage, health, attacks):
    answer = 0
    bandtime, heal, bonus = bandage
    last_time = attacks[-1][0]
    time = 0
    max_health = health
    combo = 0
    is_attacked = False
    while True:
        time += 1
        
        
        # 공격당함
        for a in attacks:
            if time == a[0]: # 공격 당할 시간이면
                is_attacked = True
                health = health - a[1]
                combo = 0
                if health <= 0:
                    return -1
                
        if time == last_time:
            break
            
        if not is_attacked:
            combo += 1
            # 1초당 힐
            health = min(max_health, health + heal)

            # 붕대 다 감음
            if combo == bandtime:
                combo = 0
                health = min(max_health, health + bonus)
        
        # print("cur time", time, "combo ", combo, "health", health, "is_attack", is_attacked)
        is_attacked = False
        
    
    return health