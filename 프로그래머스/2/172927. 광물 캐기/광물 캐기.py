def solution(picks, minerals):
    table = {
        0: {
            "diamond": 1,
            "iron": 1,
            "stone": 1,
        },
        1: {
            "diamond": 5,
            "iron": 1,
            "stone": 1,
        },
        2: {
            "diamond": 25,
            "iron": 5,
            "stone": 1,
        },
    }
    
    answer = 10**9
    l = len(minerals)
    def use_pick(mineral_idx, total):
        nonlocal answer
        if answer <= total:
            return
        
        if mineral_idx == l or sum(picks) == 0:
            if answer > total:
                answer = total
            return
        
        mj = min(mineral_idx + 5, l)
        for i in range(3):
            if picks[i] > 0:
                picks[i] -= 1
                fatigue = 0
                for j in range(mineral_idx, mj):
                    fatigue += table[i][minerals[j]]
                use_pick(mj, total+fatigue)
                picks[i] += 1
    
    use_pick(0, 0)
    return answer