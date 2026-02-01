import sys, heapq
input = sys.stdin.readline
N, M, K = map(int, input().split())
todo = []
for _ in range(N):
    heapq.heappush(todo, -int(input()))

day = 0
satisfied = []
satisfaction = 0
while todo:
    day += 1
    now = heapq.heappop(todo)
    satisfaction = satisfaction//2 - now
    satisfied.append(satisfaction)
    now += M
    if now + K < 0:
        heapq.heappush(todo, now)
print(day, *satisfied, sep='\n')