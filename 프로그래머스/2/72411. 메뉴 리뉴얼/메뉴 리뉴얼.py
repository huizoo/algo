from collections import defaultdict

def solution(orders, course):
    answer = []
    dic = {size: defaultdict(int) for size in course}
    
    for order in orders:
        order = sorted(order)
        n = len(order)
        
        for mask in range(1, 1 << n):
            size = mask.bit_count()
            
            if size not in dic:
                continue
                
            menu = []
            
            for i in range(n):
                if mask & (1 << i):
                    menu.append(order[i])
            
            dic[size][''.join(map(str, menu))] += 1
    
    for size, menus in dic.items():
        Max = 2
        candidate = []
        for menu, cnt in menus.items():
            if Max < cnt:
                candidate = [menu]
                Max = cnt
            elif Max == cnt:
                candidate.append(menu)        
        answer.extend(candidate)
        
    return sorted(answer)