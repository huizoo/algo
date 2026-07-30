def solution(queue1, queue2):
    total1 = sum(queue1)
    total2 = sum(queue2)
    target_value = (total1 + total2) // 2
    n = 2 * len(queue1)
    advanced_queue1 = queue1 + queue2
    advanced_queue2 = queue2 + queue1
    idx1 = idx2 = 0
    while idx1 < n and idx2 < n:
        if total1 > target_value:
            total1 -= advanced_queue1[idx1]
            idx1 += 1
        elif total1 < target_value:
            total1 += advanced_queue2[idx2]
            idx2 += 1
        else:
            break
    else:
        return -1
    
    return idx1+idx2