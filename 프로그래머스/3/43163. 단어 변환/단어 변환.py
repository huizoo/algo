def solution(begin, target, words):
    answer = 51
    n = len(words)
    l = len(begin)
    visited = [0]*n
    
    def dfs(now, cnt, level):
        nonlocal answer
        if now == target:
            answer = min(answer, cnt)
            return
        
        if level == n:
            return
        
        for i, word in enumerate(words):
            if visited[i]: continue
            same = 0
            for a, b in zip(now, word):
                if a == b:
                    same += 1
            if same + 1 != l: continue
            visited[i] = 1
            dfs(word, cnt+1, level+1)
            visited[i] = 0
    
    dfs(begin, 0, 0)
        
    return 0 if answer == 51 else answer