import sys
input = sys.stdin.readline

N, Q = map(int, input().split())
A = list(map(int, input().split()))

size = 1
while size < N:
    size <<= 1

tree = [0]*(2*size)

for i in range(N):
    tree[size+i] = A[i]

for i in range(size-1, 0, -1):
    tree[i] = tree[i*2] | tree[i*2+1]

def update(pos):
    idx = size + pos
    tree[idx] ^= 1
    idx //= 2
    while idx:
        tree[idx] = tree[idx*2] | tree[idx*2+1]
        idx //= 2

def query(node, start, end, l, r):
    if r < start or end < l or tree[node] == 0:
        return -1

    if start == end:
        return start

    mid = (start+end) // 2

    left = query(node*2, start, mid, l, r)
    if left != -1:
        return left

    return query(node*2+1, mid+1, end, l, r)

now = 0

for _ in range(Q):
    q = list(map(int, input().split()))

    if q[0] == 1:
        update(q[1] - 1)

    elif q[0] == 2:
        now = (now + q[1]) % N

    else:
        if tree[1] == 0:
            print(-1)
            continue

        res = query(1, 0, size-1, now, N-1)
        if res == -1:
            res = query(1, 0, size-1, 0, now-1)

        print((res - now) % N)