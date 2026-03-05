def solution(dist_limit, split_limit):
    if dist_limit == 0 or split_limit <= 1:
        return 1

    answer = 1

    p2 = 1
    for a in range(31):
        if p2 > split_limit:
            break
        p3 = 1
        for b in range(31-a):
            if p2*p3 > split_limit:
                break

            remain = dist_limit
            leaves = 1
            cap = 1

            for _ in range(a):
                if remain == 0 or cap == 0:
                    break
                x = min(cap, remain)
                remain -= x
                leaves += x
                cap = x*2

            for _ in range(b):
                if remain == 0 or cap == 0:
                    break
                x = min(cap, remain)
                remain -= x
                leaves += 2*x
                cap = x*3

            if leaves > answer:
                answer = leaves

            p3 *= 3
            
        p2 *= 2

    return answer