def solution(schedules, timelogs, startday):
    N = len(schedules)
    for i, schedule in enumerate(schedules):
        h = schedule // 100
        m = schedule % 100
        if m >= 50:
            m -= 50
            h += 1
        else:
            m += 10
        schedules[i] = h*100+m
    s = startday
    for i, timelog in enumerate(timelogs):
        schedule = schedules[i]
        for time in timelog:
            if startday in [6, 7, 13]:
                startday += 1
                continue
            startday += 1
            if time > schedule:
                N -= 1
                break
        startday = s
    
    print(schedules)
    return N