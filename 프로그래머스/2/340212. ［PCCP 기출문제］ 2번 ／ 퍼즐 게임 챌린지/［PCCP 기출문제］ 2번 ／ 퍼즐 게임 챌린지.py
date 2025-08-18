def solution(diffs, times, limit):
    Max = max(diffs)
    l = len(diffs)
    # for level in range(1, Max + 1):
    start = 1
    Min = Max

    while start <= Max:
        now = (start+Max)//2
        cnt = times[0]
        for j in range (1, l):
            gap = max(diffs[j] - now, 0)
            cnt = cnt + gap*times[j-1]+(gap+1)*times[j]
            if cnt > limit:
                start = now + 1
        if cnt <= limit:
            Min = now
            Max = now - 1


            
    return Min