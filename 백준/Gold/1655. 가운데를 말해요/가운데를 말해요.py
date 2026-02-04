import sys, heapq
input = sys.stdin.readline
N = int(input())
answer = []
max_heap = []
min_heap = []
for _ in range(N):
    x = int(input())

    if not max_heap or x <= -max_heap[0]:
        heapq.heappush(max_heap, -x)
    else:
        heapq.heappush(min_heap, x)
    
    if len(max_heap) > len(min_heap) + 1:
        heapq.heappush(min_heap, -heapq.heappop(max_heap))
    elif len(min_heap) > len(max_heap):
        heapq.heappush(max_heap, -heapq.heappop(min_heap))
    
    answer.append(-max_heap[0])

print(*answer, sep='\n')