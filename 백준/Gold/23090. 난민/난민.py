import sys, heapq
input = sys.stdin.readline

N = int(input())
answer = []
Sumx = 0
heap1, heap2 = [], []
Sum1, Sum2 = 0, 0
for i in range(1, N+1):
    x, y = map(int, input().split())
    if x > 0:
        Sumx += x
    else:
        Sumx -= x
    
    if not heap1 or y <= -heap1[0]:
        heapq.heappush(heap1, -y)
        Sum1 += y
    else:
        heapq.heappush(heap2, y)
        Sum2 += y

    l1, l2 = len(heap1), len(heap2)
    if l1 > l2+1:
        k = -heapq.heappop(heap1)
        Sum1 -= k
        heapq.heappush(heap2, k)
        Sum2 += k
    elif l2 > l1:
        k = heapq.heappop(heap2)
        Sum2 -= k
        heapq.heappush(heap1, -k)
        Sum1 += k

    mid = -heap1[0]

    answer.append(f'{mid} {Sumx+mid*len(heap1)-Sum1+Sum2-mid*len(heap2)}')
        
print(*answer, sep='\n')

