def solution(info, n, m):
    info.sort(key=lambda x: (-x[1], x[0]))
    sb = 0
    for a, b in info:
        sb += b
    if sb < m:
        return 0
    Min = 1e9
    check = set()

    def abc(level, sa, sb):
        nonlocal Min
        if sa >= n:
            return
        if sb < m:
            Min = min(sa, Min)
            return
        if level >= len(info):
            return
        state = (level, sa, sb)
        if state in check:
            return
        check.add(state)
        abc(level + 1, sa + info[level][0], sb - info[level][1])
        abc(level + 1, sa, sb)
        return

    abc(0, 0, sb)
    if Min == 1e9:
        return -1
    return Min
