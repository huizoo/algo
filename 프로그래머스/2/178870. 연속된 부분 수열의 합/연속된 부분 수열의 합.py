def solution(sequence, k):
    def move_l():
        nonlocal l, Sum
        Sum -= sequence[l]
        l += 1
        
    def move_r():
        nonlocal r, Sum
        r += 1
        Sum += sequence[r]
    
    l = r = 0
    n = len(sequence)
    sequence.append(0)
    answer = [0, n-1]
    Sum = sequence[0]
    while r < n:
        if Sum == k:
            if answer[1] - answer[0] > r - l:
                answer = [l, r]
            move_l()        
            move_r()
        elif Sum < k:
            move_r()
        elif l == r:
            move_l()
            move_r()
        else:
            move_l()
        
    return answer