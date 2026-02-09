from collections import defaultdict
import sys, heapq
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    k = int(input())
    Max = []
    Min = []
    cnt = 0
    dic = defaultdict(int)
    for _ in range(k):
        ch, n = input().split()
        if ch == 'I':
            m = int(n)
            heapq.heappush(Max, -m)
            heapq.heappush(Min, m)
            dic[m] += 1
            cnt +=1
        elif ch == 'D':
            if cnt == 0:
                continue
            if n == '1':
                while Max and dic[-Max[0]] == 0:
                    heapq.heappop(Max)
                dic[-heapq.heappop(Max)] -= 1
                cnt -= 1
                if cnt == 0:
                    Min = []
            else:
                while Min and dic[Min[0]] == 0:
                    heapq.heappop(Min)
                dic[heapq.heappop(Min)] -= 1
                cnt -= 1
                if cnt == 0:
                    Max = []
            
    if cnt == 0:
        print('EMPTY')
    else:
        while Max and dic[-Max[0]] == 0:
            heapq.heappop(Max)

        while Min and dic[Min[0]] == 0:
            heapq.heappop(Min)

        print(-Max[0], Min[0])