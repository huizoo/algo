start, end = ord('a'), ord('z') + 1
def change_alpha(num):
    return start + num % end if num >= end else num

def solution(s, skip, index):
    answer = []
    skip_set = set(ord(ch) for ch in skip)
    for ch in s:
        nxt = now = ord(ch)
        for i in range(index):
            nxt = change_alpha(nxt + 1)
            while nxt in skip_set:
                nxt = change_alpha(nxt + 1)
        if nxt >= end:
            answer.append(chr(change_alpha(nxt)))
        else:
            answer.append(chr(nxt))
    
    return ''.join(map(str, answer))