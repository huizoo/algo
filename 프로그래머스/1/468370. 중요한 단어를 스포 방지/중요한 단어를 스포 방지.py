from collections import defaultdict

def solution(message, spoiler_ranges):
    answer = 0
    words = defaultdict(int)
    message += ' '
    n = len(message)    
    spoiler_range = [0]*(n + 1)
    
    for s, e in spoiler_ranges:
        spoiler_range[s] += 1
        if e < n:
            spoiler_range[e + 1] -= 1
    
    current = 0
    for i in range(n):
        current += spoiler_range[i]
        spoiler_range[i] = 1 if current > 0 else 0
    
    masked = 0
    current_word = ''
    masked_words = set()
    for i, v in enumerate(message):
        if v != ' ':
            current_word += v
            if spoiler_range[i]:
                masked = spoiler_range[i]
        elif masked:
            masked_words.add(current_word)
            current_word = ''
            masked = 0
        else:
            words[current_word] += 1
            current_word = ''
            masked = 0
        
    for masked_word in masked_words:
        answer += 0 if words[masked_word] else 1
        
    return answer