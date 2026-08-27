def solution(n,a,b):
    '''
    n명의 참가자는 1~n까지 차례대로 배정
    12, 34, 56 이렇게 게임 진행
    이기면 진출하고 다시 번호 1~n/2 배정
    a == 1
    b == 2
    '''
    answer = 1
    while a != 1 or b != 1:
        if a%2 != 0:
            a += 1
        if b%2 != 0:
            b += 1
        a //= 2
        b //= 2
        if a == b:
            break
        answer += 1
    return answer
