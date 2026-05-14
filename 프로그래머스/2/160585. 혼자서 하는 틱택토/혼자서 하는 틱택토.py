def solution(board):
    board2 = list(''.join(row) for row in zip(*board))
    o_cnt = sum(row.count('O') for row in board)
    x_cnt = sum(row.count('X') for row in board)
    o_win = (
        'OOO' in board or
        'OOO' in board2 or
        board[0][0] == 'O' and board[1][1] == 'O' and board[2][2] == 'O' or
        board[0][2] == 'O' and board[1][1] == 'O' and board[2][0] == 'O'
    )
    x_win = (
        'XXX' in board or
        'XXX' in board2 or
        board[0][0] == 'X' and board[1][1] == 'X' and board[2][2] == 'X' or
        board[0][2] == 'X' and board[1][1] == 'X' and board[2][0] == 'X'
    )
    
    if x_cnt > o_cnt:
        return 0
    if o_cnt > x_cnt + 1:
        return 0
    if o_win and x_win:
        return 0
    if o_win and o_cnt != x_cnt + 1:
        return 0
    if x_win and o_cnt != x_cnt:
        return 0
    
    return 1