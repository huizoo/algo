import sys
input = sys.stdin.readline

N = int(input())
above = [[] for _ in range(N+1)]
below = [[] for _ in range(N+1)]
for _ in range(N-1):
    a, b, c = map(int, input().split())
    above[a].append((b, c))
    below[b].append((a, c))

root = None
for i in range(1, N+1):
    if not above[i]:
        root = i

Sum = [0]*(N+1)
Grade = [0]*(N+1)
def abc(now, sum_val):
    Sum[now] = sum_val
    if not below[now]:
        Grade[now] = sum_val
        return
    for nxt, val in below[now]:
        abc(nxt, sum_val+val)
        Grade[now] += Grade[nxt]
    if len(below[now]) == 2:
        Grade[now] -= sum_val

abc(root, 0)

Max = 0

def bbq(now, sum_val):
    global Max
    if not below[now]:
        if Max < sum_val:
            Max = sum_val
        return

    for nxt, _ in below[now]:
        bbq(nxt, sum_val+Grade[nxt])

bbq(root, Grade[root])

print(Max)