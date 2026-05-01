def solution(n, q, ans):
    answer = 0
    combination = 0
    def dfs(num, cnt):
        nonlocal answer, combination
        if cnt == 5:
            for codes, need in zip(q, ans):
                match = 0
                for c in codes:
                    if combination & (1 << c):
                        match += 1
                if match != need:
                    return
            answer += 1
            return
        if num > n:
            return
        if cnt+n-num+1 < 5:
            return
        combination |= 1 << num
        dfs(num+1, cnt+1)
        combination ^= 1 << num
        dfs(num+1, cnt)

    dfs(1, 0)
    return answer