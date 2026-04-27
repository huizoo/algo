def solution(food):
    answer = []
    for i in range(1, len(food)):
        answer.extend([i]*(food[i]//2))
    return ''.join(map(str, answer+[0]+answer[::-1]))