import heapq

def solution(k, score):
    answer = []
    heap = []
    for i, s in enumerate(score):
        if i < k:
            heapq.heappush(heap, s)
        else:
            heapq.heappushpop(heap, s)
        answer.append(heap[0])
        
    return answer