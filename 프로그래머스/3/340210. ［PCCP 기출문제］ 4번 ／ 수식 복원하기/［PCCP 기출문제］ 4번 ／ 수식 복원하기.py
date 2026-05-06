def get_min_base(*nums):
    max_digit = 0
    for num in nums:
        for ch in num:
            max_digit = max(max_digit, int(ch))
    return max(2, max_digit+1)


def change(num, base):
    if num == 0:
        return "0"
    result = []
    while num:
        result.append(num%base)
        num //= base
    return ''.join(map(str, result[::-1]))

def solution(expressions):
    answer = []
    candidate = set(range(2, 10))
    expressions_v2 = []
    
    for expression in expressions:
        exp, c = expression.split(" = ")
        
        if "+" in exp:
            a, b = exp.split(" + ")
            sign = "+"
        else:
            a, b = exp.split(" - ")
            sign = "-"
        
        if c == "X":
            expressions_v2.append(expression)
            min_base = get_min_base(a, b)
            candidate = {base for base in candidate if base >= min_base}
            continue
        
        min_base = get_min_base(a, b, c)
        
        possible = set()
        
        for base in candidate:
            if base < min_base:
                continue
                
            aa, bb, cc = int(a, base), int(b, base), int(c, base)
            
            if sign == "+":
                if aa + bb == cc:
                    possible.add(base)
            else:
                if aa - bb == cc:
                    possible.add(base)
        
        candidate &= possible
        
    
    for expression in expressions_v2:
        exp = expression.split(" = ")[0]
        
        if "+" in exp:
            a, b = exp.split(" + ")
            sign = "+"
        else:
            a, b = exp.split(" - ")
            sign = "-"
             
        candidate_v2 = set()
        
        for base in candidate:
            aa, bb = int(a, base), int(b, base)
            
            if sign == "+":
                res = aa+bb
            else:
                res = aa-bb
            
            candidate_v2.add(change(res, base))
        
        if len(candidate_v2) == 1:
            answer.append(f"{exp} = {candidate_v2.pop()}")
        else:
            answer.append(f"{exp} = ?")
            
    return answer