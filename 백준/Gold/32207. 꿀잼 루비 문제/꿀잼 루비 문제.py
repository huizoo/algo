import sys
import heapq
input = sys.stdin.readline

def solve():
    N, M, K = map(int, input().split())

    L = 21

    heap = []
    for i in range(N):
        row = list(map(int, input().split()))
        for j, x in enumerate(row):
            if len(heap) < L:
                heapq.heappush(heap, (x, i, j))
            elif x > heap[0][0]:
                heapq.heapreplace(heap, (x, i, j))

    arr = sorted(heap, reverse=True)
    nm = len(arr)

    Max = 0

    if K == 1:
        print(arr[0][0])
        return

    for i in range(nm):
        now, y, x = arr[i]
        Sum = now
        cnt = 1
        arr2 = [(y, x)]

        for j in range(i+1, nm):
            nxt, ny, nx = arr[j]

            for yy, xx in arr2:
                if abs(yy-ny) + abs(xx-nx) <= 1:
                    break
            else:
                arr2.append((ny, nx))
                Sum += nxt
                cnt += 1
                if cnt == K:
                    break

        if Max < Sum:
            Max = Sum

    print(Max)

solve()

