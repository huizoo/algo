def solution(bandage, max_health, attacks):
    skill_time, heal, heal2 = bandage
    health = max_health
    
    real_time = 0
    seq = 0
    
    for attack_time, damage in attacks:
        while 1:
            if real_time < attack_time:
                seq += 1
                if seq == skill_time:
                    seq = 0
                    health = health + heal + heal2
                else:
                    health = health + heal
                health = min(health, max_health)
            else:
                health -= damage
                if health <= 0:
                    return -1
                seq = 0
                real_time += 1
                break
            real_time += 1
            print(health)
                
            
    
    
    return health