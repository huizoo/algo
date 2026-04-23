def solution(name, yearning, photo):
    answer = []
    score = {n: y for n, y in zip(name, yearning)}
    for people in photo:
        answer.append(sum(score.get(person, 0) for person in people))
    return answer