def solution(board):    
    o_cnt = sum(1 if v == 'O' else 0 for row in board for v in row)
    x_cnt = sum(1 if v == 'X' else 0 for row in board for v in row)
    
    '''
    O 빙고 상태라면?
    o_cnt == x_cnt + 1
    '''              
    for row in board:
        if row.count('O') == 3 and o_cnt != x_cnt + 1:
            return 0
    
    for row in zip(*board):
        if row.count('O') == 3 and o_cnt != x_cnt + 1:
            return 0
    
    if (board[0][0] == board[1][1] == board[2][2] == 'O' or
        board[2][0] == board[1][1] == board[0][2] == 'O') and o_cnt != x_cnt + 1:
            return 0
    
    '''
    X 빙고 상태라면?
    o_cnt == x_cnt
    '''
    for row in board:
        if row.count('X') == 3 and o_cnt != x_cnt:
            return 0
    
    for row in zip(*board):
        if row.count('X') == 3 and o_cnt != x_cnt:
            return 0
        
    if (board[0][0] == board[1][1] == board[2][2] == 'X' or
        board[2][0] == board[1][1] == board[0][2] == 'X') and o_cnt != x_cnt:
            return 0
    '''
    빙고가 없다면?
    o_cnt == x_cnt or o_cnt == x_cnt + 1
    '''
    if not (o_cnt == x_cnt or o_cnt == x_cnt + 1):
        return 0
    
    return 1