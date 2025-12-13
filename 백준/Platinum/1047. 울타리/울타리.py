import sys
input = sys.stdin.readline

N = int(input())
trees = [tuple(map(int, input().split())) for _ in range(N)]
total_len = sum(c for _, _, c in trees)

xs = sorted(set(x for x, _, _ in trees))
ys = sorted(set(y for _, y, _ in trees))

best = N

for x1 in xs:
    for x2 in xs:
        if x1 > x2:
            continue
        for y1 in ys:
            for y2 in ys:
                if y1 > y2:
                    continue

                perimeter = 2 * ((x2 - x1) + (y2 - y1))

                cut_cnt = 0
                cut_len = 0
                inside = []

                for x, y, c in trees:
                    if x1 <= x <= x2 and y1 <= y <= y2:
                        inside.append(c)
                    else:
                        cut_cnt += 1
                        cut_len += c

                if cut_cnt >= best:
                    continue

                if cut_len >= perimeter:
                    best = cut_cnt
                    continue

                need = perimeter - cut_len
                inside.sort(reverse=True)
                extra = 0
                for c in inside:
                    need -= c
                    extra += 1
                    if cut_cnt + extra >= best:
                        break
                    if need <= 0:
                        best = min(best, cut_cnt + extra)
                        break

print(best)