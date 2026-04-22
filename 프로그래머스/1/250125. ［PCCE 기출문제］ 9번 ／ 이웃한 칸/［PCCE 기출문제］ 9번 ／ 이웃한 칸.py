d = [(0, 1), (-1, 0), (1, 0), (0, -1)]

def solution(board, h, w):
    answer = 0
    n = len(board)
    m = len(board[0])
    color = board[h][w]
    for dh, dw in d:
        nh, nw = h+dh, w+dw
        if nh < 0 or nw < 0 or nh >= n or nw >= m: continue
        if board[nh][nw] == color:
            answer += 1
    return answer