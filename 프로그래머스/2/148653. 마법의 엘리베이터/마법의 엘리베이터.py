def solution(storey):
    '''
    절대값이 10의 c제곱
    현재 위치와 버튼을 더한 결과가 0보다 작으면 움직X
    0층이 맨 아래층
    현재 민수가 있는 층에 엘베 있음
    버튼 1번당 마법의돌 1개 소모
    -1 6번 -10 1번 하면 -16이라서 7개로 16층에서 0층 갈 수 있음
    +1 4번 -10 2번 하면 -16이라서 6개로 16층에서 0층 갈 수 있음
    
    6을 0으로 맞출거냐 10으로 맞출거냐
    '''
    answer = 0
    n = len(str(storey))
    Min = 10**9
    def dfs(level, cnt, num):
        nonlocal Min
        if Min <= cnt:
            return
        
        if num == 0:
            if Min > cnt:
                Min = cnt
            return
        
        division = 10**(level+1)
        remain = num % division
        
        dfs(level+1, cnt + remain*10//division, num-remain)
        
        dfs(level+1, cnt + (division-remain)*10//division, num+(division-remain))
        
    
    dfs(0, 0, storey)
    return Min