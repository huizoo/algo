import sys
sys.setrecursionlimit(1024)

def solution(nodeinfo):
    nodes = []
    for idx, (x, y) in enumerate(nodeinfo, start = 1):
        nodes.append((x, y, idx))
    
    nodes.sort(key=lambda x: (-x[1], x[0]))
    
    tree = [[0, 0, 0] for _ in range(len(nodeinfo)+1)]
    for x, y, idx in nodes:
        tree[idx][0] = x
    
    root = nodes[0][2]
    for i in range(1, len(nodes)):
        x, y, idx = nodes[i]
        now = root
        
        while True:
            if x < tree[now][0]:
                if tree[now][1] == 0:
                    tree[now][1] = idx
                    break
                now = tree[now][1]
            else:
                if tree[now][2] == 0:
                    tree[now][2] = idx
                    break
                now = tree[now][2]
            
        
    pre = []
    post = []
    
    def preorder(now):
        if now == 0:
            return
        pre.append(now)
        preorder(tree[now][1])
        preorder(tree[now][2])
    
    def postorder(now):
        if now == 0:
            return
        postorder(tree[now][1])
        postorder(tree[now][2])
        post.append(now)
    
    preorder(root)
    postorder(root)
    
    return [pre, post]