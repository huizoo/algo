from collections import defaultdict
import sys, heapq
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    k = int(input())
    dic = defaultdict(int)
    heap = []
    heap2 = []
    for _ in range(k):
        a, b = map(str, input().split())
        b = int(b)
        if a == 'I':
            heapq.heappush(heap, b)
            heapq.heappush(heap2, -b)
            dic[b] += 1
        elif not heap or not heap2:
            continue
        elif b == 1:
            while heap2 and dic[-heap2[0]] == 0:
                heapq.heappop(heap2)
            if heap2:
                x = heapq.heappop(heap2)
                dic[-x] -= 1
        else:
            while heap and dic[heap[0]] == 0:
                heapq.heappop(heap)
            if heap:
                x = heapq.heappop(heap)
                dic[x] -= 1
    

    while heap and dic[heap[0]] == 0:
        heapq.heappop(heap)

    while heap2 and dic[-heap2[0]] == 0:
        heapq.heappop(heap2)

    if heap and heap2:
        print(-heap2[0], heap[0])
    else:
        print('EMPTY')
    