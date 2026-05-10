def time_to_second(h, m, s):
    return 60*60*h + 60*m + s


def get_hour_hand(s):
    return (s/120)%360
    

def get_minute_hand(s):
    return (s/10)%360
    
    
def get_second_hand(s):
    return (s*6)%360
    
    
def solution(h1, m1, s1, h2, m2, s2):
    answer = 0
    start, end = time_to_second(h1, m1, s1), time_to_second(h2, m2, s2)
    
    hh = get_hour_hand(start)
    mh = get_minute_hand(start)
    sh = get_second_hand(start)
    if sh == hh or sh == mh:
        answer += 1

    for time in range(start, end):
        now_hh = get_hour_hand(time)
        now_mh = get_minute_hand(time)
        now_sh = get_second_hand(time)
        nxt_hh = get_hour_hand(time+1)
        nxt_mh = get_minute_hand(time+1)
        nxt_sh = get_second_hand(time+1)
        
        if nxt_sh == 0:
            nxt_sh = 360

        m_cross = now_sh < now_mh and nxt_mh <= nxt_sh
        h_cross = now_sh < now_hh and nxt_hh <= nxt_sh
        
        if m_cross:
            answer += 1
        if h_cross:
            answer += 1

        if m_cross and h_cross and (time+1)%43200 == 0:
            answer -= 1

    return answer