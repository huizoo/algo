def solution(s):
    answer = []
    a = ord('a')
    bef = [-1]*26
    for i, c in enumerate(s):
        idx = ord(c)-a
        answer.append(i-j if (j:= bef[idx]) >= 0 else -1)
        bef[idx] = i
    return answer