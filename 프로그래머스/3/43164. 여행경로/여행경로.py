from collections import defaultdict, Counter

def solution(tickets):
    dic = defaultdict(Counter)

    tickets.sort()
    
    for a, b in tickets:
        dic[a][b] += 1

    l = len(tickets) + 1

    answer = []
    candidate = ['ICN']

    def dfs(now):
        nonlocal answer

        if len(candidate) == l:
            if not answer or candidate < answer:
                answer = candidate[:]
            return

        for nxt in dic[now]:
            if dic[now][nxt] == 0:
                continue

            dic[now][nxt] -= 1
            candidate.append(nxt)

            dfs(nxt)

            candidate.pop()
            dic[now][nxt] += 1

    dfs('ICN')

    return answer