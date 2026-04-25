def date_parser(date):
    y, m, d = map(int, date.split('.'))
    return y*12*28 + m*28 + d

def solution(today, terms, privacies):
    answer = []
    today = date_parser(today)
    terms_dictionary = {term[:1]: int(term[2:]) for term in terms}
    for idx, privacy in enumerate(privacies, start = 1):
        start_date, term = privacy.split()
        if today >= date_parser(start_date) + terms_dictionary[term] * 28:
            answer.append(idx)
    return answer