def solution(sequence, k):
    answer = [0, len(sequence) - 1]
    Sum = 0
    l = 0
    for r, v in enumerate(sequence):
        Sum += v
                       
        while Sum > k:
            Sum -= sequence[l]
            l += 1
        
        if Sum == k and answer[1] - answer[0] > r - l:
            answer = [l, r]
        
    return answer