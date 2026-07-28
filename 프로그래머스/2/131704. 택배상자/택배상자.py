def solution(order):
    answer = 0
    sub_last = 0
    truck = 1
    used = [0]*(len(order)+1)
    for o in order:
        if truck == o:
            used[truck] = 1
            truck += 1
        elif sub_last == o:
            used[sub_last] = 1
            while used[sub_last]:
                sub_last -= 1
        elif sub_last+1 < o:
            sub_last = o-1
            used[o] = 1
            truck = o+1
        else:
            break
            
    answer = sum(used)
    return answer