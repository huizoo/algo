def solution(diffs, times, limit):
    answer = 0
    def can_play(level):
        total_time = 0
        for i, (diff, time) in enumerate(zip(diffs, times)):
            if diff > level:
                total_time += (diff-level)*(time+times[i-1])+time
            else:
                total_time += time
            if limit < total_time:
                return False
        return True
        
        
    l, r = 1, max(diffs)
    
    while l < r:
        mid = (l+r)//2
        if can_play(mid):
            r = mid
        else:
            l = mid+1
            
    return l