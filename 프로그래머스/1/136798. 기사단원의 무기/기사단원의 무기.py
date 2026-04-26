def solution(number, limit, power):
    answer = 1
    number += 1
    factor_cnt = [2]*(number)
    factor_cnt[0] = 0
    for i in range(2, number):
        answer += cnt if (cnt:= factor_cnt[i]) <= limit else power
        for j in range(2*i, number, i):
            factor_cnt[j] += 1
    
    return answer