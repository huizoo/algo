def solution(n, costs):
    answer = 0
    costs.sort(key=lambda x: x[2])
    
    par = list(range(n))
    
    def findboss(a):
        if par[a] == a:
            return a
        par[a] = findboss(par[a])
        return par[a]
    
    def unionfind(a, b):
        bossA, bossB = findboss(a), findboss(b)
        
        if bossA == bossB:
            return 0
        
        par[bossA] = bossB
        return 1
    
    for a, b, cost in costs:
        if unionfind(a, b):
            answer += cost
        
    return answer