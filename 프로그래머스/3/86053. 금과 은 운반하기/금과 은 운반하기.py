def solution(a, b, g, s, w, t):
    def pos(time):
        gold = silver = total = 0
        for gi, si, wi, ti in zip(g, s, w, t):
            move = time//(2*ti)
            if time%(2*ti) >= ti:
                move += 1
            can_move = move * wi
            gold += min(gi, can_move)
            silver += min(si, can_move)
            total += min(gi + si, can_move)
        return gold >= a and silver >= b and total >= a + b
        
    left, right = 0, 2 * max(t) * (a + b)
    while left < right:
        mid = (left + right) // 2
        if pos(mid):
            right = mid
        else:
            left = mid + 1
        
    return left