def solution(n, times):
    l = 0
    r = max(times) * n
    while l < r:
        mid = (l + r) // 2
        
        if sum(mid//t for t in times) >= n:
            r = mid
        else:
            l = mid + 1

    return l