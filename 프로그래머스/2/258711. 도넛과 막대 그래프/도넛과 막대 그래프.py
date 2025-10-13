from collections import defaultdict, deque

def solution(edges):
    answer = [0, 0, 0, 0]
    indeg = defaultdict(int)
    outdeg = defaultdict(int)
    graph = defaultdict(list)
    nodes = set()

    for a, b in edges:
        outdeg[a] += 1
        indeg[b] += 1
        graph[a].append(b)
        nodes.add(a)
        nodes.add(b)

    for v in nodes:
        if indeg[v] == 0 and outdeg[v] >= 2:
            answer[0] = v
            break

    starts = graph[answer[0]]
    visited = set()

    for s in starts:
        if s in visited:
            continue
        q = deque([s])
        v_count = 0
        e_count = 0
        sub_nodes = set()
        while q:
            x = q.popleft()
            if x in sub_nodes:
                continue
            sub_nodes.add(x)
            v_count += 1
            for nxt in graph[x]:
                if nxt == answer[0]:
                    continue
                e_count += 1
                q.append(nxt)
        visited |= sub_nodes
        if e_count == v_count:
            answer[1] += 1
        elif e_count == v_count - 1:
            answer[2] += 1
        elif e_count == v_count + 1:
            answer[3] += 1

    return answer
