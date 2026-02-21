import sys, heapq
input = sys.stdin.readline

N = int(input())
arr = sorted([tuple(map(int, input().split())) for _ in range(N)])

heap = []
for s, t in arr:
    if heap and heap[0] <= s:
        heapq.heappop(heap)
    heapq.heappush(heap, t)

print(len(heap))
