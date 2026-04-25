def date_parser(date):
    year, month, day = date.split('.')
    return int(year), int(month), int(day)

def is_have_to_delete(year, month, day, year2, month2, day2):
    if year > year2:
        return 1
    elif year == year2:
        if month > month2:
            return 1
        elif month == month2:
            if day >= day2:
                return 1
    return 0

def end_date(year, month, day, term):
    nxt_month = month + term
    if nxt_month % 12 == 0:
        return year + nxt_month // 12 - 1, 12, day
    else:
        return year + nxt_month // 12, nxt_month % 12, day

def solution(today, terms, privacies):
    answer = []
    terms_dict = dict()
    for term in terms:
        t1, t2 = term.split()
        terms_dict[t1] = int(t2)
    ty, tm, td = date_parser(today)
    for idx, privacy in enumerate(privacies, start = 1):
        start_date, t = privacy.split()
        ey, em, ed = end_date(*date_parser(start_date), terms_dict[t])
        if is_have_to_delete(ty, tm, td, ey, em, ed):
            answer.append(idx)
            
    return answer