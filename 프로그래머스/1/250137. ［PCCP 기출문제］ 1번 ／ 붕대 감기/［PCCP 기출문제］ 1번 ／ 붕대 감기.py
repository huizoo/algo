def solution(bandage, health, attacks):   
    casting_time, heal_amount, additional_heal_amount = bandage
    max_health = health
    time = 0
    
    for attack_time, attack_damage in attacks:
        heal_time = attack_time - time - 1
        time = attack_time
        additional_cnt = heal_time // casting_time
        health = min(max_health,
                     health + heal_time * heal_amount + additional_cnt * additional_heal_amount) \
                 - attack_damage
        
        if health <= 0:
            return -1
    
    return health