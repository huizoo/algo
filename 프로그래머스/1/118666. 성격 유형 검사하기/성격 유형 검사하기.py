from collections import defaultdict

def solution(survey, choices):
    answer = ''
    score = {1: 3, 2: 2, 3: 1, 4: 0, 5: -1, 6: -2, 7: -3}
    personality = defaultdict(int)
    for _, ((v1, _), c) in enumerate(zip(survey, choices)):
        personality[v1] += score[c]
    
    answer += 'R' if personality['R'] >= personality['T'] else 'T'
    answer += 'C' if personality['C'] >= personality['F'] else 'F'
    answer += 'J' if personality['J'] >= personality['M'] else 'M'
    answer += 'A' if personality['A'] >= personality['N'] else 'N'
    
    return answer