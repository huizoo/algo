import sys
input = sys.stdin.readline
N = int(input())
dic = {
    'P': 0,
    'C': 0,
    'V': 0,
    'S': 0,
    'G': 0,
    'F': 0,
    'O': 0,
}
for _ in range(N):
    st = input().rstrip()
    Set = set(st)
    l = len(st)
    if len(Set) == 1:
        dic[next(iter(Set))] += l
    else:
        dic['O'] += l

P, C, V, S, G, F = map(int, input().split())
O = int(input())
print(dic['P']*min(P, O) + dic['C']*min(C, O) + dic['V']*min(V, O) + dic['S']*min(S, O) + dic['G']*min(G, O) + dic['F']*min(F, O) + dic['O']*O)
