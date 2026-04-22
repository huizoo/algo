def solution(players, callings):
    rank = {player: i for i, player in enumerate(players)}
    for calling in callings:
        back = rank[calling]
        front = back - 1
        rank[calling] -= 1
        rank[players[front]] += 1
        players[front], players[back] = players[back], players[front]
        
    return players