from collections import defaultdict
import heapq

def solution(genres, plays):
    answer = []
    dic = defaultdict(int)
    dic2 = defaultdict(list)
    for i, (genre, play) in enumerate(zip(genres, plays)):
        dic[genre] += play
        heapq.heappush(dic2[genre], (-play, i))
    
    for k, v in sorted(dic.items(), key=lambda x: x[1], reverse=True):
        for _ in range(min(2, len(dic2[k]))):
            answer.append(heapq.heappop(dic2[k])[1])
            
    return answer