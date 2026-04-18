def solution(k, m, score):
    answer = 0
    n = len(score)
    score.sort(reverse=True)
        
    for i in range(0, n-n%m, m):
        Min = min(score[i:i+m])
        answer += Min*m  
    
    return answer