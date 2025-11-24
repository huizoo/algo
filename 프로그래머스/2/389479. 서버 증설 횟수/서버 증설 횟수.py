def solution(players, m, k):
    answer = 0
    arr = [0 for _ in range(24)]
    for i in range(24):
        필요서버 = players[i] // m
        if arr[i] >= 필요서버: continue
        더필요서버 = 필요서버 - arr[i]
        answer += 더필요서버
        for j in range(i, i+k):
            if j >= 24: break
            arr[j] += 더필요서버
            
    return answer