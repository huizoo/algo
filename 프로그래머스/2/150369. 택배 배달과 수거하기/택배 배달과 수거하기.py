def solution(cap, n, deliveries, pickups):
    answer = 0
    di = pi = n - 1
    dlist = []
    plist = []

    while di >= 0:
        while di >= 0 and deliveries[di] == 0:
            di -= 1

        if di < 0:
            break

        remain = cap
        far = di
        remove = 0

        while di >= 0 and remain - deliveries[di] >= 0:
            remain -= deliveries[di]
            remove += deliveries[di]
            di -= 1

        if di >= 0 and remain > 0:
            deliveries[di] -= remain
            remove += remain

        if remove > 0:
            dlist.append(far)

    while pi >= 0:
        while pi >= 0 and pickups[pi] == 0:
            pi -= 1

        if pi < 0:
            break

        remain = cap
        far = pi
        remove = 0

        while pi >= 0 and remain - pickups[pi] >= 0:
            remain -= pickups[pi]
            remove += pickups[pi]
            pi -= 1

        if pi >= 0 and remain > 0:
            pickups[pi] -= remain
            remove += remain

        if remove > 0:
            plist.append(far)

    if len(dlist) < len(plist):
        dlist += [0] * (len(plist) - len(dlist))
    else:
        plist += [0] * (len(dlist) - len(plist))

    for d, p in zip(dlist, plist):
        answer += max(d, p) + 1

    return 2 * answer