def solution(order):
    answer = 0
    sub = [0]
    truck = 1
    n = len(order)
    
    for o in order:
        while truck <= n and truck <= o:
            sub.append(truck)
            truck += 1
        
        if sub[-1] == o:
            sub.pop()
            answer += 1
        else:
            break
    
    return answer