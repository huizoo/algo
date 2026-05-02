def solution(cost, hint):
    answer = 10**15
    n = len(cost)
    k = len(hint[0])
    stock = [0]*n
    def clear_stage(stage, total_cost):
        nonlocal answer
        if total_cost >= answer:
            return
        if stage == n:
            if total_cost < answer:
                answer = total_cost
            return
        can_use = min(stock[stage], n-1)
        clear_stage(stage + 1, total_cost + cost[stage][can_use])
        if stage == n-1:
            return
        hint_cost = hint[stage][0]
        for i in range(1, k):
            stock[hint[stage][i]-1] += 1
        clear_stage(stage + 1, total_cost + hint_cost + cost[stage][can_use])
        for i in range(1, k):
            stock[hint[stage][i]-1] -= 1
    
    clear_stage(0, 0)
    
    return answer