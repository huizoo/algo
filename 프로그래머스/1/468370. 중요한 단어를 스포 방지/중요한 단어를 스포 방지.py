def solution(message, spoiler_ranges):
    answer = 0
    dic = dict()
    for x in message.split():
        if x in dic:
            dic[x] += 1
        else:
            dic[x] = 1
    n = len(message)
    visited = [0]*n
    for l, r in spoiler_ranges:
        while l >= 0 and message[l] != ' ':
            l -= 1
        while r < n and message[r] != ' ':
            r += 1
        start = -1
        for x in range(l+1, r):
            if visited[x]: continue
            visited[x] = 1
            if start == -1:
                if message[x] == ' ': continue
                start = x
            elif message[x] == ' ':
                word = message[start:x]
                
                if dic[word] == 1:
                    answer += 1
                else:
                    dic[word] -= 1
                start = -1
        
        if start != -1:
            word = message[start:r]
            if dic[word] == 1:
                answer += 1
            else:
                dic[word] -= 1
        
        
    return answer