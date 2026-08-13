import heapq

def solution(n, k, enemy):
    length = len(enemy)
    
    if k >= length:
        return length
    
    heap = []
    total = 0

    for i, v in enumerate(enemy):
        if total + v <= n:
            heapq.heappush(heap, -v)
            total += v
        elif k > 0:
            k -= 1                
            if heap and -heap[0] > v:
                total += heapq.heappop(heap) + v
                heapq.heappush(heap, -v)
        else:                
            return i
        
    return length