'''
최소 필요 피로도, 소모 피로도가 있음
'''


def solution(k, dungeons):
    answer = 0
    l = len(dungeons)
    def dfs(remain, cnt, visited):
        nonlocal answer
    
        if answer < cnt:
            answer = cnt
        
        for nxt in range(l):
            if 1 << nxt & visited == 1 << nxt: continue
            if dungeons[nxt][0] > remain: continue
            dfs(remain - dungeons[nxt][1] , cnt + 1, visited | 1 << nxt)
        
    for i in range(l):
        if dungeons[i][0] > k: continue
        dfs(k - dungeons[i][1], 1, 1 << i)
            
    return answer