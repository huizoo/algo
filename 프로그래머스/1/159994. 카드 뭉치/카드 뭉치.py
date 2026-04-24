def solution(cards1, cards2, goal):
    idx1 = idx2 = 0
    n1 = len(cards1); n2 = len(cards2)
    for target in goal:
        if idx1 < n1 and cards1[idx1] == target:
            idx1 += 1
        elif idx2 < n2 and cards2[idx2] == target:
            idx2 += 1
        else:
            return "No"
            
    return "Yes"