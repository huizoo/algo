def solution(keymap, targets):
    answer = []
    keymap_dictinary = dict()
    for i, row in enumerate(keymap):
        for j, v in enumerate(row):
            if v in keymap_dictinary:
                keymap_dictinary[v] = min(j + 1, keymap_dictinary[v])
            else:
                keymap_dictinary[v] = j + 1
                
    for target in targets:
        cnt = 0
        for ch in target:
            if n:= keymap_dictinary.get(ch, 0):
                cnt += n
            else:
                cnt = -1
                break
        answer.append(cnt)
        
    return answer