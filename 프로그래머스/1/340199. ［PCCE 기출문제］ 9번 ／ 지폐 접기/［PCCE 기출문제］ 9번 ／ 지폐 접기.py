def solution(wallet, bill):
    answer = 0
    max_w, min_w = max(wallet), min(wallet)
    b1, b2 = bill
    
    while max_w < max(b1, b2) or min_w < min(b1, b2):
        if b1 < b2:
            b2 //= 2
        else:
            b1 //= 2
        answer += 1
    return answer