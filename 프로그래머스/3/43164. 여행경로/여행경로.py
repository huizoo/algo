from collections import defaultdict

def solution(tickets):
    answer = []
    route = defaultdict(list)
    
    for s, e in tickets:
        route[s].append(e)
    
    for key in route.keys():
        route[key].sort(reverse=True)
    
    def dfs(now):
        while route[now]:
            dfs(route[now].pop())
        answer.append(now)
    
    dfs("ICN")
    
    return answer[::-1]