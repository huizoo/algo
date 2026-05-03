def get_bit_count(num):
    return bin(num).count('1')


def solution(n, infection, edges, k):
    answer = 1
    nodes = {
        0: [[] for _ in range(n+1)],
        1: [[] for _ in range(n+1)],
        2: [[] for _ in range(n+1)]
    }
    for x, y, t in edges:
        nodes[t-1][x].append(y)
        nodes[t-1][y].append(x)
    
    dp = [set() for _ in range(k+1)]
    dp[0].add(1 << infection)
    
    for i in range(k):
        for mask in dp[i]:
            for t in range(3):
                nxt_mask = mask
                stack = []
                for bit in range(1, n+1):
                    if (mask >> bit) & 1:
                        stack.append(bit)
                
                while stack:
                    now = stack.pop()
                    
                    for nxt in nodes[t][now]:
                        if (nxt_mask >> nxt) & 1: continue
                        nxt_mask |= 1 << nxt
                        stack.append(nxt)
                    
                dp[i+1].add(nxt_mask)
    
    for mask in dp[-1]:
        answer = max(answer, get_bit_count(mask))
        
    return answer