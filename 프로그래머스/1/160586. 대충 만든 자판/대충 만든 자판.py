def solution(keymap, targets):
    answer = []
    keymap_dictionary = dict()
    for row in keymap:
        for j, v in enumerate(row):
            if v in keymap_dictionary:
                keymap_dictionary[v] = min(j + 1, keymap_dictionary[v])
            else:
                keymap_dictionary[v] = j + 1
                
    for target in targets:
        cnt = 0
        for ch in target:
            if n:= keymap_dictionary.get(ch, 0):
                cnt += n
            else:
                cnt = -1
                break
        answer.append(cnt)
        
    return answer