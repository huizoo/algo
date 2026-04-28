def solution(a, b, g, s, w, t):
    def pos(time):
        gold = silver = total = 0
        for gi, si, wi, ti in arr:
            move = time//(2*ti)
            if time%(2*ti) >= ti:
                move += 1
            can_move = move * wi
            gold += min(gi, can_move)
            silver += min(si, can_move)
            total += min(gi + si, can_move)
        return gold >= a and silver >= b and total >= a + b
        
    arr = list(zip(g, s, w, t))
    left, right = 0, 10**15
    while left < right:
        mid = (left + right) // 2
        if pos(mid):
            right = mid
        else:
            left = mid + 1
        
    return left